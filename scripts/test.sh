#! /bin/bash

sudo apt update
sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venf 
. ./venf/bin/activate
pip3 install -r requirements.txt

cd ./service-two
python3 -m pytest --cov application
cd ..

cd ./service-three
python3 -m pytest --cov application
cd ..

cd ./service-four
python3 -m pytest --cov application
cd ..




