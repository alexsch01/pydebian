sudo apt update
sudo apt install -y wget make
wget https://github.com/alexsch01/pydebian/releases/download/python2.7/Python-2.7.tar.xz
tar -xf Python-2.7.tar.xz
cd Python-2.7
sudo make altinstall
cd ..
sudo rm -rf Python-2.7*
# sudo rm /usr/local/bin/2to3-3.11
# sudo rm /usr/local/bin/idle3.11
# sudo rm /usr/local/bin/pip3.11
# sudo rm /usr/local/bin/python3.11-config
