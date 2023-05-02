#!/bin/bash

export DRONE_APP_PATH=/home/drone-app

sudo apt-get update
sudo apt-get -y install python3
sudo apt-get -y install python3-pip
pip3 install -r requirements.txt