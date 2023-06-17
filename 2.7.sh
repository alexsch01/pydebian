sudo apt update
sudo apt install -y wget make binutils
wget https://github.com/alexsch01/pydebian/releases/download/python2.7/Python-2.7.tar.xz
tar -xf Python-2.7.tar.xz
cd Python-2.7
sudo make altinstall
cd ..
sudo rm -rf Python-2.7*
sudo rm /usr/local/bin/2to3
sudo rm /usr/local/bin/idle
sudo rm /usr/local/bin/pydoc
sudo rm /usr/local/bin/python2.7-config
sudo rm /usr/local/bin/smtpd.py
