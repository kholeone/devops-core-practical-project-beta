
# Practical Project  👞👟🥾🥿👠👡🩰

## Resources 
- Application: http://35.197.234.35:5000/ 
- Board: https://trello.com/b/5CriV5R7/snkrs-app  

### Brief
To create an application that generates “Objects” upon a set of predefined rules, by creating a service-orientated architecture for an application. It is to be composed of four services that work together.
#### Additional Requirements
- An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.

-  To provide a record of any issues or risks that was faced creating the project.

-  An Application fully integrated using the Feature-Branch model into a Version Control System which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.

- If a change is made to a code base, then Webhooks would be used so that Jenkins recreates and redeploys the changed application

- The project must follow the Service-oriented architecture that has been asked for.

- The project must be deployed using containerisation and an orchestration tool.

- Create an Ansible Playbook that will provision the environment that the application needs to run.

- The project will make use of a reverse proxy to make the application accessible to the user.

#### My Approach
The approach to have the service –orientated architecture was to create an application that has #2 and #3 service generating a random object. This is in a form of a string, as this application is based on footwear and the 2nd service will generate a brand i.e “Nike” while the 3rd service will generate a shoe model i.e “Air Max 1”. Service #4 will combine those results of the generated words and dictate with that information if its a real shoe, if so it will return information of the retail price and even a description of what the shoe is. However if the randomised objects gives a mix matched result it will display to the user that the shoe does not exist. The 1st Service will of course render these results with the Jinja 2 templates being the foundation of the 3 services communicating with each other.

### Architecture

#### Diagrams
![alt text](https://github.com/kholeone/devops-core-practical-project-beta/blob/main/documents/App%20architecture.png)

#### CI Pipeline
There has been a few iterations of the pipeline as the use of more tools become avaliable when diving further into the project. Initialy from just reading the project specifications a CI Pipeline was developed to have an idea of what could be expected from just analysing the scope what needs to be done and implemented in order to fufill the needs for the project.
#### 1st Version
![alt text](https://github.com/kholeone/devops-core-practical-project-beta/blob/main/documents/Screenshot%202020-12-07%20130939.png)
#### 2nd version
The general idea with the CI Pipeline is that Python pushes the source code using Git, creating a repostitory on Git-Hub. This is being tracked throughout the project by the Kandan Board to ensure the implmentations done for the project has been done and can focus on areas that need to be completed. When this is pushed to Jenkins, it is also configuered with a webhook that allow Jenkins build jobs to be to automatically build after a commit has been pushed to the Version Control Provider. Now at the CI Server using the Jenkins Pipeline it will then go through multiple stages of the application, one being testing which is handled by Pytest and then building and pushing the images using docker-compose, storing on Docker-Hub. These same images are then pulled by docker-swarm that deploys a stack from the virtual machine, using nginx as a load balancer and a reverse proxy.
![alt text](https://github.com/kholeone/devops-core-practical-project-beta/blob/main/documents/Screenshot%202020-12-07%20153321.png)


##### Version Control System
There was full utilisation of the feature-branch model throughout the duration of the project. This help to separate the aspects of the development in smaller increments and have a clear analysis of what has been added. All the feature-branches were used during the first stages of the development doing something as simple as adding code, tests, configuring docker files etc. I treated this branch model as if an individual was giving only one area of the project in their full control while not interfering the process of another which will reduce any problems from the project failing due to errors and no track of meaningful implementations.
![alt text](https://github.com/kholeone/devops-core-practical-project-beta/blob/main/documents/version-control-branches.png "branch models")

#### CI Server Jenkins Pipeline
This is the Jenkins pipeline process that ensures the project is functional and ready for deployment. The testing stage will run a test on each service to ensure everything works as intended. The second stage starts to build the application by using docker to have multiple containers that can run a single service, along with pushing it which will lead to the next stage. Deployment is the final stage which pulls the images and retrieves the project to be rolled out. There were multiple stages, however it seemed to be best to minise it as much as possible since it allowed for full deployment. This meant that implementations that were used had to be taken out as it potentially broked the process of the stages. With the time contraints the option was to maxmimise the most of what can be done and a simple three stage build was the conclusion.
![alt text](https://github.com/kholeone/devops-core-practical-project-beta/blob/development/documents/deployment.png "stage-view-jenkins-pipeline")
![alt text](https://github.com/kholeone/devops-core-practical-project-beta/blob/main/documents/Screenshot%202020-12-07%20115036.png)

#### Cloud server: GCP virtual machines
Google Cloud Platform was used for the virtual machines of this project, I set it up by having the vm-demo-2 as my development machine that I would SSH into from my local machine as it was easier to devlop using Visual Studio Code and more efficient. This machine was the foundation to the project which created the manager and worker virtual machines which utilise the tool docker swarm which was a requirement for this project. These machines will also have access to ports such as 5000 for the flask application and 8080 for jenkins as it was needed for the project. ![alt text](https://github.com/kholeone/devops-core-practical-project-beta/blob/main/documents/GCP%20virtual%20machines.png)

##### Docker
Docker was used for containerisation and an orchestration tool in this project. Docker-Compose built all four services and tagged them. It makes use of a Dockerfile that builds a Docker Image which contains all the dependancies the application requires. The services then start which has been defined and can be accessed to users. The tool used for this was Docker-Hub as it stored the repositories of the services and can build and update upon them when rolling an update.
![alt text](https://github.com/kholeone/devops-core-practical-project-beta/blob/main/documents/docker-hub.png)


### Project Tracking 
A Kanban board was produced using Trello. This helped to manage the project by displaying the tasks that has been completed, in completed along with risks that has happened during the duration of the project. This gave a good idea of what areas of focus needs to be paid attention too along with giving updates on the current situation of the project.
![alt text](https://github.com/kholeone/devops-core-practical-project-beta/blob/development/documents/kanban-board.png)

### Risk Assessment
The potential of risks and threats in projects is not uncommon, so a risk assessment was done to give awareness of any possible outcomes and to be able to counter the problems that will ensure the success of a project. It is beneficial to know how to react to a problem as it can make a difference to how it is effectively handled which can save a development from an unforeseen consequence by being prepared and having the consideration of safe practices to negate any potential risk.
![alt text](https://github.com/kholeone/devops-core-practical-project-beta/blob/main/documents/risk-assessment.png "Risk Assessment")

### Testing 
Testing was done with all of the four services. This was done using Pytest to attain a high percentage of coverage to ensure each service runs correctly with minimal problems/bugs. This was first done after the application on its own was completed, doing the tests in the terminal and confirming the results in there before going on to the next stage of the project. However, this was also done again for the Jenkins Pipeline as it was the early steps used before the deployment of the project. Ensuring that if it was to fail the deployment will be a failure, thus no risk of putting out a defective application that may cause harm in the long run.
![alt text](https://github.com/kholeone/devops-core-practical-project-beta/blob/development/documents/testing.png "pytest --cov")

### Build
During the build stage, docker login will begin this stage following a stop and rmi- all for any previous containers, networks, volumes and images. It will then do a docker-compose build and push it to a repository that is used on Docker-Hub.
![alt text](https://github.com/kholeone/devops-core-practical-project-beta/blob/main/documents/jenkins-pipeline%20build.png)
[alt text](https://github.com/kholeone/devops-core-practical-project-beta/blob/main/documents/jenkins-pipeline%20build2.png)

### Deploy
This is the final stage will ssh the manager and start to pull all four services individually along with an nginx. It will then clone down the projects repository and deploy a new stack using the docker stack deploy. 

### Front-End Design
The front end design is very minimal, as it was not the core focus of the project there was a little consideration of the design. It has a neat layout which provides easy navigation but very light weight that matches the functions of the application.

![alt text](https://github.com/kholeone/devops-core-practical-project-beta/blob/development/documents/front-end-1.png "snkrs-app front end")
This is the index/home page of the application which have the title of the application and a link to generate the object which is a shoe model.
![alt text](https://github.com/kholeone/devops-core-practical-project-beta/blob/development/documents/front-end-2%20.png "snkrs-app front end")
Since it is random it compiles with a numerous number of variations, so if the conditions are not met; being that it is an actual shoe model that does not exist the message displayed from the 4th service that using the pre-defined rules.
![alt text](https://github.com/kholeone/devops-core-practical-project-beta/blob/development/documents/front-end-3.png "snkrs-app front end")
This is another variation of what the user can see, if it is a real shoe model it will display information to the user which can be in a form of the real retail price of the shoe or information/history of what the shoe is.

### Known Issues
-	The application seems to have a timeout at times when refreshed repeatably 

### Future Improvements
With the time duration of this project, only so much can get dome and of course this always amounts to areas of improvements that can be done. Although I am satisfied with what has been achieved during the time period this project was developed on, with less/no constraints I would have had future improvements such as: 

-	To have a more interesting front end design
-	Make full utilisation of the technologies that was involved in this project
- Perhaps more stages to the Jenkins Pipeline that can make it more effective
- 



### Authors
Kholeo Taylor 👻




