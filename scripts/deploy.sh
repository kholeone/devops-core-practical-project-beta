#! /bin/bash

docker pull kholeone/service-one:latest
docker pull kholeone/service-two:latest
docker pull kholeone/service-three:latest
docker pull kholeone/service-four:latest
docker stack deploy --compose-file docker-compose.yaml snkrs-app
