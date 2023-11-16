/*
Copyright 2023.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

package controller

import (
	"context"

	corev1 "k8s.io/api/core/v1"
	//apierrors "k8s.io/apimachinery/pkg/api/errors"
	"k8s.io/apimachinery/pkg/runtime"
	"k8s.io/klog"
	ctrl "sigs.k8s.io/controller-runtime"
	"sigs.k8s.io/controller-runtime/pkg/client"
	"sigs.k8s.io/controller-runtime/pkg/log"
)

// PodReconciler reconciles a Pod object
type PodReconciler struct {
	client.Client
	Scheme *runtime.Scheme
}

//+kubebuilder:rbac:groups=core,resources=pods,verbs=get;list;watch;create;update;patch;delete

// Reconcile is part of the main kubernetes reconciliation loop which aims to
// move the current state of the cluster closer to the desired state.
// TODO(user): Modify the Reconcile function to compare the state specified by
// the Pod object against the actual cluster state, and then
// perform operations to make the cluster state reflect the state specified by
// the user.
//
// For more details, check Reconcile and its Result here:
// - https://pkg.go.dev/sigs.k8s.io/controller-runtime@v0.16.0/pkg/reconcile
/*
Go does not have classes. However, you can define methods on types.
A method is a function with a special receiver argument.
In this case r is a reciver argument which means we can reference the methods of PodReconciler using the r object in the Reconcile function
*/
func (r *PodReconciler) Reconcile(ctx context.Context, req ctrl.Request) (ctrl.Result, error) {
	_ = log.FromContext(ctx)

	// TODO(user): your logic here //method is called whenever a Pod is created, updated, or deleted
	//A nil error denotes success; a non-nil error denotes failure.
	var pod corev1.Pod
	if err := r.Get(ctx, req.NamespacedName, &pod); err != nil {
		//this gets called if there is an error calling r.Get with default value for ctrl.Result and non-not-found error being returned
		return ctrl.Result{}, client.IgnoreNotFound(err)
	}
	//this gets called if r.Get is a success
	klog.Infof("Pod Name : %s Image: %s Status: %s Labels: %v", pod.Name, pod.Spec.Containers[0].Image, pod.Status.Phase, pod.Labels)
	return ctrl.Result{}, nil
}

// SetupWithManager sets up the controller with the Manager.
// The SetupWithManager method is called when the operator starts. It serves to tell the kubebuilder framework what types our PodReconciler needs to watch
// in this case PodReconciler needs to watch pods
func (r *PodReconciler) SetupWithManager(mgr ctrl.Manager) error {
	return ctrl.NewControllerManagedBy(mgr).
		For(&corev1.Pod{}).
		Complete(r)
}
