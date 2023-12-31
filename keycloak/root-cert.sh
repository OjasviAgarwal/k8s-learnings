# create a folder to store certificates
mkdir -p .ssl
# generate an rsa key
openssl genrsa -out .ssl/root-ca-key.pem 2048
# generate root certificate
openssl req -x509 -new -nodes -key .ssl/root-ca-key.pem -days 3650 -sha256 -out .ssl/root-ca.pem -subj "/CN=kube-ca"