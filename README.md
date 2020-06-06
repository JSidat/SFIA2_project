# SFIA2_project

## Table of contents

* [Introduction](#Introduction)
* [Project Scope](#Project-Scope)
* [Technology constraints](#Technology-constraints)
* [Risk Assessment](#Risk-Assessment)
* [Deployment](#Deployment)
* [Testing](#Testing)
* [Conclusion](#Conclusion)


## Introduction

The prupose of this project was to create four microservices that work together with one service acting as the core service which will allow a user to interact with the application. Services 2 and 3 were to generate a random object each, both of which will be used by the last service to generate the final object.

## Project Scope

## Project Scope

The scope of the project outlines the minimum requirements to successfully complete the project and assesses our development against SFIA.
The minimum requirements for the project are outlined as follows:

* Project Tracking via a kanban style board such as trello that identifies the user story, use cases and progression of the project over a period of time.

* Use of the feature-branch model in a version control system which is connected to a CI server via a webhook and eventually deployed onto a cloud-based virtual machine

* Service must be deployed using containerisation via docker and deployed via a CI/CD server, Jenkins.

* An ansible playbook must be used to provide the environment the application is run in.

## Technology Constraints

* Kanban Board: Asana or an equivalent Kanban Board
* Version Control: Git
* CI Server: Jenkins
* Configuration Management: Ansible
* Cloud server: GCP virtual machines
* Containerisation: Docker
* Orchestration Tool: Docker Swarm
