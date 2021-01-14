#!/bin/bash
haproxy_path=/etc/haproxy/certs

for hostname in {{ letsencrypt_domainlist | join(" ") }}; do
    cert_path=/etc/letsencrypt/live/$hostname/

    echo "Generuji certifikat pro $hostname"

    certbot --text --agree-tos --email flidr@webeo.cz certonly --standalone -d $hostname --non-interactive --http-01-port 9999 | grep "Congratulations"
    if [ $? -eq 0 ]; then
        cat $cert_path/{fullchain.pem,privkey.pem} > $haproxy_path/$hostname.pem
        systemctl reload haproxy
    fi
    echo
done