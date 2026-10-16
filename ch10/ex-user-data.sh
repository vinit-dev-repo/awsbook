#!/bin/bash
dnf install -y httpd
echo "<h1>the exercise page</h1>" > /var/www/html/index.html
systemctl enable --now httpd
