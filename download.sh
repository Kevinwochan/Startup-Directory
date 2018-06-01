#!/bin/sh
# download default logo image
$(curl https://upload.wikimedia.org/wikipedia/commons/9/93/No-logo.svg > public/media/logos/undefined.svg)
# download navbar logo
$(curl https://textbook.ventures/wp-content/uploads/2018/03/TBV-Logo-Horizontal-56PX.png > public/static/img/textbook-ventures.png)
# download tbv icon
$(curl https://textbook.ventures/wp-content/uploads/2018/03/cropped-TBV-Logo-Icon-Only-Dark-BG@2x-1-32x32.png> public/static/img/textbook-ventures-icon.png)
