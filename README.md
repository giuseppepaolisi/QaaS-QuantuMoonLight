![ezgif com-gif-maker](https://user-images.githubusercontent.com/21276583/174580320-c1fd36fc-0cdc-4f59-9ca8-a877059b21ff.gif) 

This repository was developed for the exam of Cloud Computing 22/23, UNISA <br>
QuantuMoonLight: A QaaS Platform to experiment typical Machine Learning pipeline through Quantum Computers

<h1>QuantuMoonLight</h1>

QuantuMoonLight is the major user-friendly web platform aimed at quantum computation and machine learning enthusiasts, industry professionals, students and researchers.

The main function of the system is to allow registered users to perform common operation as validation, preprocessing, classifications, regression and more on datasets uploaded by users.

Quantum Machine Learning is a little-known area and therefore we want to extend the interested community, trying to offer a product simple, reliable and useful, using the solutions made available by newest Quantum Computing and Cloud Computing technologies

The goal of the project is to observe the variation of the metrics of a quantum classification algorithm by applying preprocessing techniques that decrease the dimensionality of a dataset in favor of execution time.

Due to this automation of mechanisms, this project enable a new area of computer science that aims to ease software practitioners to intercat with typical pipeline of machine learning 

The purpose of this project is to provide through the paradigm “Quantum-as-a-Services” the Machine Learning algorithms used in the QML platform: from validation and feature engineering methods to the creation and use of the quantum classification model .

<h2>Local Installation</h2>
The following prerequisites must be used to install such a platform locally:
<ul>
<li>Python >= vers. 3.8;</li>
<li>Anaconda >= vers. 2021.11;</li>
<li>Editor to set up the code (example PyCharm);</li>
<li>MySql vers. >= 7.0;</li>
<li>MySQL Client(example HeidiSQL);</li>
</ul>

After verifying that you have these prerequisites you will need to proceed in this order:

   <h4>If you want to run on IDE:</h4>
<ol>
<li> Import the repository on your IDE (ex. using https://github.com/giuseppepaolisi/QaaS-QuantuMoonLight)</li>
<li> Open Anaconda Prompt and install the environment.yml using this command (you can find in ./env/yourOS/environment.yml)<br>
   "conda env create -f environment.yml"
<li> Set-up the interpreter and the environment on your IDE as a Flask Application</li>
<li>Run the code</li>
<li>Click the link (usually) http://0.0.0.0:5000, the home page will be shown on your browser</li>
</ol>
   <h4>Else if you want to run on prompt:</h4>
   <ol>
<li> clone the github repository</li> (git clone https://github.com/giuseppepaolisi/QaaS-QuantuMoonLight)
<li>Open Anaconda Prompt and install the environment.yml using this command (you can find in ./env/yourOS/environment.yml)<br>
   "conda env create -f environment.yml" <br>
   next activate the environment<br>
   "conda activate environment-name"</li>
<li>cd into the QuantuMoonLight folder of the local copy of the repository</li>
<li>type in "flask run" and run it</li>
<li>open the link provided by the cli interface to access your local copy of QuantuMoonLight</li>
   </ol>

   
 

