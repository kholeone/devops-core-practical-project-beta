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


