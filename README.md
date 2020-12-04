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

#### Database Structure
Here is a Entity relationship diagram (ERD). This is the final database structure chosen to build with the application.
It is able to store all the information in the database, able to create, read, update and delete everything associated database.

![alt text](https://github.com/kholeone/devops-core-fundamental-project-/blob/main/Documents/erd_ver_1.0.png)

#### CI Pipeline
The CI pipeine allows implementation efficiently, showing that coding devlopment has been doing in python, able to be pushed and pulled to the git version control system. Trello is keeping track of the current development which then cycles forward to the CI server Jenkins that updates the enviroment through automation.
Testing was done through this along with the application being deployed on a virtual machine with gunicorn intergration acessing mySQL databases.

![alt text](https://github.com/kholeone/devops-core-fundamental-project-/blob/main/Documents/Screenshot%202020-11-16%20081716.png "CI Pipeline")

### Project Tracking 
This is the Trello board used throughout the duration of the project. Utilising it to help track the development of the project. This has been 
very helpful as it displays what needs to be done and what has been completed, focusing on the areas of the projects that need requires attention the most.
![alt text](https://github.com/kholeone/devops-core-fundamental-project-/blob/main/Documents/Screenshot%202020-11-15%20025715.png)

Here is a link to my Trello board, that was used to track the progress of the project:
https://trello.com/b/9r3rbJG2/lucky-duck-app


### Risk Assessment
The Risk Assessment was done to prepare, anticipate and deliver the reliefs of potential threats that can occur with the project.
![alt text](https://github.com/kholeone/devops-core-fundamental-project-/blob/main/Documents/risk_assessment_snippet.png "risk assessment")
Risk Assessment link: 
https://drive.google.com/file/d/18dbeBYOijlBn2jIVVrRpjJASh52iZTPC/view?usp=sharing

### Testing 
Testing has been done with Pytest, used in Python in a form of Unit Testing.
This is to analyse and detect differences in existing and required conditions, and to evaluate the features of the application.

![alt text](https://github.com/kholeone/devops-core-fundamental-project-/blob/main/Documents/Screenshot%202020-11-15%20223302.png "unit testing")

81% was achieved in the Unit Testing. There are areas of improvement in the testing which lies in the '**applications.routes.py**', but as it stands
it was not huge of an issue to have the application fail as it is still functional. Integration testing was also produced later in the testing phase which test different parts of the application work together. This was used mainly to test the CRUD aspects of the application.


### Front-End Design
The front end design is very minimal, as it was not the core focus of the project there was a little consideration of the design. It has a neat layout which provides easy navigation but very light weight that matches the functions of the application.

![alt text]("snkrs-app front end")
![alt text]("snkrs-app front end")
![alt text]("snkrs-app front end")

### Known Issues
- An issue with updating the details of a listing
- When updating text, additional string characters are present
- Adding a detail within a listing that has already been done will cause an error

### Future Improvements
There are many improvements that can be made to the application
assuming having less time constraints and broadening of knowledge.
Improvements such as:

- Having a login for sellers that want to create a listing.
- Allow pictures to be uploaded to display the product.
- Have a messaging system where users can publically or privately message each   other in regards of the listing.
- Have a stylistic front-end design to make the application more appealing
- Produce an application that was close to the original concept 
- To have an application with minimal bugs

### Authors
Kholeo Taylor 👻




