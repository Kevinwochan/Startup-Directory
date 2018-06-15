#!/bin/sh
# Update files to the latest repo
$(chmod +x *.sh) 
$(./update.sh)
# Sanity checking firewall permisions
$(sudo ufw allow 'Apache Full')
# Restart Apache
$(sudo systemctl restart apache2)
# Download default logo image
$(mkdir ./public/media)
$(mkdir ./public/media/logos/)
$(curl https://upload.wikimedia.org/wikipedia/commons/9/93/No-logo.svg > ./public/media/logos/undefined.svg)
# download navbar logo
$(mkdir ./public/static)
$(mkdir ./public/static/img)
$(curl https://textbook.ventures/wp-content/uploads/2018/03/TBV-Logo-Horizontal-56PX.png > ./public/static/img/textbook-ventures.png)
# download tbv icon
$(curl https://textbook.ventures/wp-content/uploads/2018/03/cropped-TBV-Logo-Icon-Only-Dark-BG@2x-1-32x32.png> ./public/static/img/textbook-ventures-icon.png)
