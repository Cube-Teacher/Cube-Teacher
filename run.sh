#!/bin/bash

# execute sol.py 
cd ./public/img
python3 sol.py &

cd ..
cd ..

# sleep for 2 sec
sleep 2

# execute cam.py to start Flask server for streaming
python3 cam.py

# execute index.js 
node index.js