
from kubernetes import client, config

def main():
    aToken = ""
    aConfiguration = client.Configuration()
    aConfiguration.host = "https://127.0.0.1:16443"
    aConfiguration.verify_ssl = False
    aConfiguration.api_key = {"authorization": "Bearer " + aToken}
    aApiClient = client.ApiClient(aConfiguration)
    v1 = client.CoreV1Api(aApiClient)
    pod_list = v1.list_namespaced_pod("dex")
    for pod in pod_list.items:
        print("%s\t%s\t%s" % (pod.metadata.name,
                              pod.status.phase,
                              pod.status.pod_ip))

if __name__ == '__main__':
    main()