#!/bin/bash

export DRONE_APP_PATH=/home/drone-app

sudo apt -y install python3 python3-pip
pip3 install -r requirements.txt
mkdir ${DRONE_APP_PATH}/drone-src
sudo cp -r . ${DRONE_APP_PATH}/drone-src