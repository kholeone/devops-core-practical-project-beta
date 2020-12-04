#! /bin/bash
sudo apt update
sudo apt install python3 python3-pip 

cd ./service-two
pip3 install -r requirements.txt
python3 -m pytest --cov application
cd ..

cd ./service-three
python3 -m pytest --cov application
cd ..

cd ./service-four
python3 -m pytest --cov application
cd ..




