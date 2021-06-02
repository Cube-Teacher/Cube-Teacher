#!/bin/bash

# execute sol.py 
cd ./public/img
python3 sol.py

cd ..
cd ..

# sleep for 2 sec
sleep 2

# execute index.js 
node index.js