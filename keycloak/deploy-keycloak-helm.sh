helm upgrade --install --wait --timeout 15m --namespace keycloak --repo https://charts.bitnami.com/bitnami keycloak keycloak --reuse-values --values - <<EOF
auth:
  createAdminUser: true
  adminUser: admin
  adminPassword: admin
  managementUser: manager
  managementPassword: manager
proxyAddressForwarding: true
ingress:
  enabled: true
  hostname: keycloak.kind.cluster
  annotations:
    kubernetes.io/ingress.class: nginx
  tls: true
  extraTls:
  - hosts:
    - keycloak.kind.cluster
    secretName: keycloak.kind.cluster-tls
postgresql:
  enabled: true
  postgresqlPassword: password
EOF