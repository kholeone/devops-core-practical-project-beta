#! /bin/bash
sudo docker-compose down --rmi all
sudo docker-compose build 
docker-compose down --rmi all
docker-compose build 
sudo docker login 
sudo docker-compose push 
