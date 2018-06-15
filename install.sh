#!/bin/sh

### FUNCTIONS

# Download default images
download(){
	# Download default logo image
	$(mkdir ./public/media)
	$(mkdir ./public/media/logos/)
	$(curl https://upload.wikimedia.org/wikipedia/commons/9/93/No-logo.svg > ./public/media/logos/undefined.svg)
	# Download navbar logo
	$(mkdir ./public/static)
	$(mkdir ./public/static/img)
	$(curl https://textbook.ventures/wp-content/uploads/2018/03/TBV-Logo-Horizontal-56PX.png > ./public/static/img/textbook-ventures.png)
	# Download tbv icon
	$(curl https://textbook.ventures/wp-content/uploads/2018/03/cropped-TBV-Logo-Icon-Only-Dark-BG@2x-1-32x32.png> ./public/static/img/textbook-ventures-icon.png)
}

# Install python3 and or apache2 dependencies
installDependencies(){
	$(sudo apt-get update;)
	if [ "$1" = "dev" ]
	then
		echo "Installing python3 and pipenv"
		$(sudo apt-get install python3-pip pipenv;)
	fi
	
	if [ "$1" = "server" ]
	then
		echo "Installing Apache2 and Mod-wsgi-py3"
		$(sudo apt-get install libapache2-mod-wsgi-py3;)
	fi
}

# Update files to the latest repo
update(){
	$(chmod +x *.sh; ./update.sh)
	# Sanity checking firewall permisions
	$(sudo ufw allow 'Apache Full')
}

### install.sh - A script to set up django on a new server or a dev environment
if [ "$1" = "dev" ]
then
    echo "Installing dev environment"
elif [ "$1" = "server" ]
then
    echo "Installing server environment"
else
	echo "No commandline argument was entered, please use either dev or server"
fi

download
installDependencies
update

# Restart Apache
$(sudo systemctl restart apache2)
