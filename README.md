# SFIA2_project

## Table of contents

* [Introduction](#Introduction)
* [Project Scope](#Project-Scope)
* [Technology constraints](#Technology-constraints)
* [Trello Board](#Trello-Board)
* [Risk Assessment](#Risk-Assessment)
* [Data Persistence](#Data-Persistence)
* [Deployment](#Deployment)
* [Testing](#Testing)
* [Areas for improvememt](#Areas-for-improvement)
* [Conclusion](#Conclusion)


## Introduction

The purpose of this project was to create four microservices that work together with one service acting as the core service which will allow a user to interact with the application. Services 2 and 3 were to generate a random object each, both of which will be used by the last service to generate the final object.


## Project Scope

The scope of the project outlines the minimum requirements to successfully complete the project and assesses our development against SFIA.
The minimum requirements for the project are outlined as follows:

* Project Tracking via a kanban style board such as trello that identifies the user story, use cases and progression of the project over a period of time.

* Use of the feature-branch model in a version control system which is connected to a CI server via a webhook and eventually deployed onto a cloud-based virtual machine

* Service must be deployed using containerisation via docker and deployed via a CI server, Jenkins.

* An ansible playbook must be used to provide the environment the application is run in.

## Technology Constraints

* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm

## Trello Board

A kanban board was used to manage workflow and keep on top of tasks that were to be completed in order to successfully complete the project. Agile methodologies were implemented where applicable as set out in the brief. For example, having a sprint backlog and defining user stories. Due to the solo nature of the project, a lot of the scrum framework could not be implemented. MoSCow prioritisation was implemented in the kanban board, where everything labelled red was deemed to be high priority as these tasks were directly related to meeting the minimum requirements and producing the minimum viable product. As the tasks were completed the were transferred along the kanban board, giving a good visual representation of progress throughout the project.

### Initial Kanban Board 

![Initial Kanban Board](https://github.com/JSidat/SFIA2_project/blob/master/screenshots/2020-06-13%20(4).png)


### Final Kanban Board

![Final Kanban Board](https://github.com/JSidat/SFIA2_project/blob/master/screenshots/2020-06-13%20(5).png)


## Risk Assessment

The risk assessement allows for planning of possible events that could occur that negatively impact the project and stop someone from completing any part of a job. It outlines event or risks that could potentially occur whilst working on a project. It also briefly explains what the consequence of the risk would be. The deductions section of the risk assessment puts forward possible actions that can be taken to counter the risk and neutralise any issues the risk might cause. The outcome section is a follow up on deductions and tells us what we expect to happen if we carry put the correct precautionary measures to stop the risk from occurring. Each risk was plotted on a matrix where two factors were taken into account, the severity of the risk, and the likelihood of the risk occurring. Any risk that had a high possibility of occurrence coupled with high severity would be plotted in the red area of the colour coded matrix. Any risk placed in the green is likely to be something that is tolerable and won't have huge negative impact on the project.

![Initial Risk Assessment](https://github.com/JSidat/SFIA2_project/blob/master/screenshots/2020-06-14.png)

### Revised risk assessment

As the project progressed I made some revisions to my risk assessment, which showed that my initial risk assessment could have been a bit more detailed in certain aspects, especially situational aspects brought about by the current unique pandemic situation and how that would affect performance and productivity. As a result, the revised risk assessment addresses these issues a bit further, as these issues were things that I was dealing with as the project  progressed, which made this follow-up quite organic and relevant to the unexpected situation we find ourselves in. 

![Revised Risk Assessment](https://github.com/JSidat/SFIA2_project/blob/master/screenshots/2020-06-14%20(2).png)

## Data Persistence

A very simple database was used to store the final object created in service 4, the final team name. This meant that if the service was stopped and started again, the previous objects created would still be visible on the homescreen and stored in the database. This was quite simple to acheive but essential as it was a requirement as part of the minimum viable product. 

![Database table](https://github.com/JSidat/SFIA2_project/blob/master/screenshots/2020-06-14%20(3).png)

## Deployment

Deployment of the project was the main focus of the modules covered. The ultimate goal was to automate deployment of a containerised application in a manner where if an update was to be added to the application, the service would not be affected whilst the update was occuring. 

The DevOps tools that were taught as in modules for this project were used together to containerise the application to make the application more portable between different clouds and platforms. Other benefits of containerisation include being much more efficient in terms of resources being used compared to VM's. Also security can be improved with this approach as the applications are isolated from each other as well as the host system.

![Deployment pipeline](https://github.com/JSidat/SFIA2_project/blob/master/screenshots/2020-06-14%20(4).png)

## Testing

Basic unit testing was carried out. The intention was to carry out full unit testing and integration testing and implement mock testing into the project as well. However, due to some last minute application issues, time allocated for testing was used up for debugging and fixing errors. Testing was carried out for service 2 and 3, however full testing was not achieved for services 1 and 4 as mock testing would be required to achieve adequate coverage of interactions such as get requests.

![Service 1 test](https://github.com/JSidat/SFIA2_project/blob/master/screenshots/2020-06-13%20(2).png)

![service 2 test](https://github.com/JSidat/SFIA2_project/blob/master/screenshots/2020-06-13.png)

![service 3 test](https://github.com/JSidat/SFIA2_project/blob/master/screenshots/2020-06-13%20(1).png)

![service 4 test](https://github.com/JSidat/SFIA2_project/blob/master/screenshots/2020-06-13%20(3).png)


## Areas for improvement

* Further testing is definitely required to determine whether the app is working how it should and if all the parts of the app are wokring together how they should. Automating tests using jenkins is also another area where improvements could be made
* Making the application a bit more complex would test my understanding of the concepts and tools learned in the module as the app itself is quite simple. This was done on purpose as I wanted to focus on the DevOps tools rather then spend too much time on the flask appllication.
* possibily having more nodes and using NGINX for live production, and having a reverse proxy between port 80 and port 5000 of the frontend container.
* Add more functionality to the website to make the website more useful and add possible user stories.

## Conclusion

Overall I found the project quite challenging, mainly due to the volume of content being delivered and the pace it was being delivered at. I thoroughly enjoyed learning about these new tools and more importantly, how useful they are by applying the skills to a practical project. The project gave us a taste of the kind of work we'd experience in the real world where having a constantly working website, even when deploying updates, is extremely important. I look forward to further developing my skills and learning more about this extrememly exciting field. 
