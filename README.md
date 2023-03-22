# QuantuMoonlight

![ezgif com-gif-maker](https://user-images.githubusercontent.com/21276583/174580320-c1fd36fc-0cdc-4f59-9ca8-a877059b21ff.gif) 
###### This repository was developed for the exam of Cloud Computing 22/23, UNISA
##### QuantuMoonLight: A QaaS Platform to experiment typical Machine Learning pipeline through Quantum Computers




**Indice dei contenuti:**

- [What is QuantuMoonLight](#what-is-quantumoonlight)
- [Azure Cloud Services](#azure-cloud-services)
- [How to install with Docker](#how-to-install-with-docker)


## What is QuantuMoonLight

QuantuMoonLight is the major user-friendly web platform aimed at quantum computation and machine learning enthusiasts, industry professionals, students and researchers.

The main function of the system is to allow registered users to perform common operation as validation, preprocessing, classifications, regression and more on datasets uploaded by users.

Quantum Machine Learning is a little-known area and therefore we want to extend the interested community, trying to offer a product simple, reliable and useful, using the solutions made available by newest Quantum Computing and Cloud Computing technologies

The goal of the project is to observe the variation of the metrics of a quantum classification algorithm by applying preprocessing techniques that decrease the dimensionality of a dataset in favor of execution time.

Due to this automation of mechanisms, this project enable a new area of computer science that aims to ease software practitioners to intercat with typical pipeline of machine learning

The purpose of this project is to provide through the paradigm “Quantum-as-a-Services” the Machine Learning algorithms used in the QML platform: from validation and feature engineering methods to the creation and use of the quantum classification model .

## Azure Cloud Services

### Azure WebApp
To host the application on web by taking the advantage of cloud app services
### Azure SQL DB
To store the data of the application by taking the advantage of cloud db services
### Azure DevOps
We have developed a pipeline to build, test and deploy application automatically and taking the other advantage in interation between team member
### Azure Container Registry
To host the docker image by taking the advantage of azure environment integration between services used
### Azure DNS
To improve facility and accessability on the website by taking the advantage of the azure provider


## How to install with Docker
###### Do this steps with terminal only for first execution

 1. Clone git project:
```c
git clone https://github.com/giuseppepaolisi/QaaS-QuantuMoonLight.git && cd QaaS-QuantuMoonLight
```
 2. Build Docker image
```c
 docker build -t <YourDockerRepository>/quantumoonlight:latest .
```
 3. Create and start the container
```c
docker run -d -p 5000:5000 --name <ChooseContainerName> <YourDockerRepository>/quantumoonlight:latest
```

###### Do this steps after the steps upside

1. Start container
```c
docker start <ContainerName>
```
3. Stop container
```c
docker stop <ContainerName>
```
Copyright © 2023
[Giuseppe Paolisi](https://github.com/giuseppepaolisi)
[Gennaro Alessio Robertazzi](https://github.com/Robertales).

   
 



   
 

