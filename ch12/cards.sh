ip -o link | awk -F": " '{print $2}' | grep -v lo | paste -sd" " -
ip -4 -o addr show | grep -v "127.0.0.1" | wc -l
