#!/bin/bash

# install flask
pip3 install flask

# install numpy
pip3 install numpy

# install nodejs and npm
curl -sL https://deb.nodesource.com/setup_14.x | sudo bash -
sudo apt install nodejs
sudo apt install build-essential

# show version
npm -v
node -v