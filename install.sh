#!/bin/bash

# check if we are root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root(Sorry)"
   exit 1
fi

#not the best way to do this, but this is my first time.
#give me a break
mkdir /usr/src/python-imager/
cp -f main.py /usr/src/python-imager/main.py
echo "python /usr/src/python-imager/main.py "\$1" "\$2" "\$3 > "/usr/src/python-imager/run.sh"
chmod -f 775 /usr/src/python-imager/run.sh
ln -f -s /usr/src/python-imager/run.sh /usr/bin/python-imager
chmod -f 775 /usr/bin/python-imager

echo "Installation complete!"
