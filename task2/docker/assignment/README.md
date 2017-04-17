# How to run a docker image
## Create a dockerfile

* Do **touch dockerfile**
* **touch dockerfile**
>>>>>>> b3001a95e43aefa3c86758404762651d5a742b17
* Create your python script **script.py**
* Add the following to dockerfile
* **FROM python:3** 
* **ADD my_script.py /**
* **CMD ["python", "./script.py"]**
* run **docker build -t docker-task .**
* **docker-task** is the name of the container
* Check if the container has been created
* run **docker images**
* then run **docker run docker-task**
