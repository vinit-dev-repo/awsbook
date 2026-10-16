#!/bin/bash
dnf install -y -q nginx
echo "<h1>built into the image</h1>" > /usr/share/nginx/html/index.html
systemctl enable --now nginx
