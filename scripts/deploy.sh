#!/bin/bash
ssh manager << EOF
docker pull kholeone/service-one:latest
docker pull kholeone/service-two:latest
docker pull kholeone/service-three:latest
docker pull kholeone/service-four:latest
docker pull nginx:alpine
git clone https://github.com/kholeone/devops-core-practical-project-beta
docker stack deploy --compose-file docker-compose.yaml snkrs-app
EOF