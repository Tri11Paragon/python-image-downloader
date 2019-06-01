#!/bin/bash

#CONFIG(You can modify these)

install_dir="/usr/share/python-imager/"

#DO NOT CHANGE ANYTHING BELOW THIS LINE
#----------------[==================]----------------

# check if we are root
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root(Sorry)"
   exit 1
fi

#not the best way to do this, but this is my first time.
#give me a break
rm -fr $install_dir
mkdir $install_dir
cp -f main.py $install_dir/main.py
#echo "python $install_dir/main.py "\$1" "\$2" "\$3" "\$4" "\$5" "\$6" "\$7" "\$8" "\$9" "\${10}" "\${11}" "\${12}" "\${13}" "\${14}" "\${15}" "\${16}" "\${17}" "\${18}" "\${19}" "\${20} > "$install_dir/run.sh"
#chmod -f 775 $install_dir/run.sh
chmod -f 775 $install_dir/main.py
ln -f -s $install_dir/main.py /usr/bin/python-imager
chmod -f 775 /usr/bin/python-imager

echo "Installation complete!"
