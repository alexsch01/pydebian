sudo apt update
sudo apt install -y wget make
wget https://github.com/alexsch01/pydebian/releases/download/python3.11/Python-3.11.tar.xz
tar -xf Python-3.11.tar.xz
cd Python-3.11
sudo make altinstall
cd ..
sudo rm -rf Python-3.11*
sudo rm /usr/local/bin/2to3-3.11
sudo rm /usr/local/bin/idle3.11
sudo rm /usr/local/bin/pydoc3.11
sudo rm /usr/local/bin/pip3.11
sudo rm /usr/local/bin/python3.11-config
