#!/bin/bash
dnf install -y -q nginx
TOKEN=$(curl -s -X PUT http://169.254.169.254/latest/api/token -H "X-aws-ec2-metadata-token-ttl-seconds: 300")
AZ=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/placement/availability-zone)
echo "served by $(hostname) in $AZ" > /usr/share/nginx/html/index.html
cat > /etc/nginx/conf.d/book.conf <<'NG'
server {
  listen 8080;
  root /usr/share/nginx/html;
  location /health { return 200 "ok\n"; }
}
NG
systemctl enable --now nginx
