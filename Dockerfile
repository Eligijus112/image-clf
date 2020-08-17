# Getting the base image
FROM python:3.7 

# Updating any possible package in the base image
RUN apt-get update

# Copying over the local files to the container
COPY . /app 

# Setting the working directory as the 'app' directory 
WORKDIR /app 

# Installing all the packages needed for the python app 
RUN pip install -r requirements.txt 