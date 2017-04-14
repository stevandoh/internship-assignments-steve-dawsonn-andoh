#How to run a dockerfile

##Create a dockerfile

* **touch dockerfile**
Add the following to dockerfile
* **FROM python:2** 
* **ADD my_script.py /**
* **CMD ["python", "./my_script.py"]**
* run **docker build -t hello-docker .**
hello-docker is the name of the container
Check if the container has been created
* run **docker images**
* then run ** docker run hello-docker **
