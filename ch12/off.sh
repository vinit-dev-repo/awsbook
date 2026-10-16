curl -s -m 3 -o /dev/null -w "%{http_code}\n" http://169.254.169.254/latest/meta-data/instance-type
