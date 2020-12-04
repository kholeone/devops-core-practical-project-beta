#!/bin/bash
sudo docker login
sudo docker-compose stop --rmi all
sudo docker-compose build
docker-compose push