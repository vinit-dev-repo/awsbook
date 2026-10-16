#!/bin/bash
dnf install -y -q nginx stress-ng
TOKEN=$(curl -s -X PUT http://169.254.169.254/latest/api/token -H "X-aws-ec2-metadata-token-ttl-seconds: 300")
AZ=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/placement/availability-zone)
ID=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/instance-id)
echo "version 1 on $(hostname) in $AZ" > /usr/share/nginx/html/index.html
cat > /etc/nginx/conf.d/book.conf <<'NG'
server {
  listen 8080;
  root /usr/share/nginx/html;
  add_header X-Served-By $hostname always;
  location /health { return 200 "ok\n"; }
}
NG
systemctl enable --now nginx
for i in $(seq 1 60); do
  STATE=$(curl -s -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/autoscaling/target-lifecycle-state)
  if [ "$STATE" = "InService" ]; then
    aws autoscaling complete-lifecycle-action --lifecycle-hook-name awsbook-ch17-launch --auto-scaling-group-name awsbook-ch17-asg --lifecycle-action-result CONTINUE --instance-id "$ID" --region us-east-1 || true
    break
  fi
  sleep 5
done
