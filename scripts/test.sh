#! /bin/bash

cd ./service-one
python3 -m pytest --cov application
cd ..

cd ./service-two
python3 -m pytest --cov application
cd ..

cd ./service-three
python3 -m pytest --cov application
cd ..

cd ./service-four
python3 -m pytest --cov application
cd ..




