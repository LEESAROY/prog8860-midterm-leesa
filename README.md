# prog8860-midterm-leesa

# Repository structure
We have created the repository prog8860-midterm-leesa
We have the below files:

Jenkinsfile: It contains the stages and their configurations of jenkins pipeline.

Dockerfile: It contains the instructions to build the Docker image.

requirements.txt: It contains Python dependencies.

midterm.py: This is the Flask application.

test_midterm.py: This is the Unit test file for the Flask application.

ci.yml: This contains the stages and configurations of Github Action pipeline.

We have 2 branches, main and feature/python-jenkins.

# To run the application
First we need to run: git clone https://github.com/LEESAROY/prog8860-midterm-leesa.git
cd prog8860-midterm-leesa

to install the dependacies:
python -m pip install --upgrade pip
pip install -r requirements.txt

to run the app:
python midterm.py

to run the unittest:
python -m unittest test_midterm.py

in the browser:
then we have to go to http://localhost:5000/

# This app will display below message 
"This is midterm exam!"


# Running the Github Action pipeline
We have configured the ci.yml file in such a way so whenever we will push anything to the feature branch or create a pull request to master then it will get triggered automatically.
We can re-run the job also from Action -> workflows
Also we can check the previous builds.

# Pulling the Docker Image from the Registry

login into dockerhub:
docker login -u <your-docker-username> -p <your-docker-password>

pull the image:
docker pull leesa007/python-jenkins:latest

create the container:
docker run -p 5000:5000 leesa007/python-jenkins:latest

in the browser:
we can check in http://localhost:5000/ It will display "This is midterm exam!"

# Running the Jenkins Pipeline
We need to install Jenkins and need to make sure it can access the github repository.
We can go to Jenkins Dashboard
We need to create a new Pipeline job
Inside the pipeline configuration we can use the repository URL https://github.com/LEESAROY/prog8860-midterm-leesa.git and set the script path to `Jenkinsfile`. Also we can mention the checkout branch name.
We can trigger the build manually by clicking on 'build now'.
