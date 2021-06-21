#!/bin/bash

# install flask
pip3 install flask

# install opencv
# important:
#           Please check your opencv is 4.x.x
#           If you are 3.x.x will get error!
pip3 install opencv-python
sudo apt install libatlas-base-dev

# install apriltag
pip3 install pupil_apriltags

# install numpy
pip3 install numpy

# 
pip3 install imutils

# install nodejs and npm
curl -sL https://deb.nodesource.com/setup_14.x | sudo bash -
sudo apt install nodejs
sudo apt install build-essential

# show version
npm -v
node -v