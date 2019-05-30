#!/bin/bash

# check if we are root
if [[ $EUID -ne 0 ]]; then
	echo "This script must be run as root (again sorry)"
	exit 1
fi

git pull

bash install.sh
