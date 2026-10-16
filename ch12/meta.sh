curl -s -o /dev/null -w "%{http_code}\n" http://169.254.169.254/latest/meta-data/instance-type
curl -s http://169.254.169.254/latest/meta-data/instance-type; echo
curl -s http://169.254.169.254/latest/meta-data/tags/instance/Name; echo
curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone; echo
curl -s http://169.254.169.254/latest/meta-data/iam/security-credentials/; echo
curl -s http://169.254.169.254/latest/meta-data/iam/security-credentials/awsbook-ch12-role | grep -oE '"(Code|Type)" : "[A-Za-z-]+"'
curl -s -o /dev/null -w "%{http_code}\n" http://169.254.169.254/latest/meta-data/spot/instance-action
curl -s http://169.254.169.254/latest/dynamic/instance-identity/document | grep -oE '"(region|instanceType)" : "[a-z0-9.-]+"'
curl -s http://169.254.169.254/latest/meta-data/ | head -5
