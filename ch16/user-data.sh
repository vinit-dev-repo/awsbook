#!/bin/bash
dnf install -y -q nginx
TOKEN=$(curl -s -X PUT http://169.254.169.254/latest/api/token -H "X-aws-ec2-metadata-token-ttl-seconds: 60")
AZ=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/placement/availability-zone)
echo "hello from $(hostname) in $AZ" > /usr/share/nginx/html/index.html
mkdir -p /usr/share/nginx/html/api
echo "api on $(hostname)" > /usr/share/nginx/html/api/index.html
cat > /etc/nginx/conf.d/book.conf <<'NG'
server {
  listen 8080;
  root /usr/share/nginx/html;
  add_header X-Served-By $hostname always;
  add_header X-Seen-Forwarded-For $http_x_forwarded_for always;
  add_header X-Seen-Forwarded-Proto $http_x_forwarded_proto always;
  add_header X-Seen-Forwarded-Port $http_x_forwarded_port always;
  location /health { return 200 "ok\n"; }
}
server {
  listen 8081 proxy_protocol;
  root /usr/share/nginx/html;
  add_header X-Served-By $hostname always;
  add_header X-Seen-Client $proxy_protocol_addr always;
  location /health { return 200 "ok\n"; }
}
NG
systemctl enable --now nginx
