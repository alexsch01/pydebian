sudo apt update
sudo apt install -y wget make
wget https://github.com/alexsch01/pydebian/releases/download/python3.10/Python-3.10.tar.xz
tar -xf Python-3.10.tar.xz
cd Python-3.10
sudo make altinstall
cd ..
sudo rm -rf Python-3.10*
sudo rm /usr/local/bin/2to3-3.10
sudo rm /usr/local/bin/idle3.10
sudo rm /usr/local/bin/pip3.10
sudo rm /usr/local/bin/python3.10-config
