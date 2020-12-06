#!/bin/bash
ssh manager << EOF
sudo docker pull kholeone/service-one:latest
sudo docker pull kholeone/service-two:latest
sudo docker pull kholeone/service-three:latest
sudo docker pull kholeone/service-four:latest
sudo docker pull nginx:alpine
sudo git clone https://github.com/kholeone/devops-core-practical-project-beta
cd devops-core-practical-project-beta
sudo docker stack deploy --compose-file docker-compose.yaml snkrs-app
EOF

