#!/bin/bash

# check if we are root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root(Sorry)"
   exit 1
fi

#not the best way to do this, but this is my first time.
#give me a break
rm -fr /usr/src/python-imager/
mkdir /usr/src/python-imager/
cp -f main.py /usr/src/python-imager/main.py
echo "python /usr/src/python-imager/main.py "\$1" "\$2" "\$3" "\$4" "\$5" "\$6" "\$7" "\$8" "\$9" "\${10}" "\${11}" "\${12}" "\${13}" "\${14}" "\${15}" "\${16}" "\${17}" "\${18}" "\${19}" "\${20} > "/usr/src/python-imager/run.sh"
chmod -f 775 /usr/src/python-imager/run.sh
ln -f -s /usr/src/python-imager/run.sh /usr/bin/python-imager
chmod -f 775 /usr/bin/python-imager

echo "Installation complete!"
