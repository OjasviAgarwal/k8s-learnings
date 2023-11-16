# install ingress-nginx
helm upgrade --install --wait --timeout 15m \
  --namespace ingress-nginx --create-namespace \
  --repo https://kubernetes.github.io/ingress-nginx \
  ingress-nginx ingress-nginx \
  --values - <<EOF
defaultBackend:
  enabled: true
EOF