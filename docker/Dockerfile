# Download base image ubuntu 18.04
FROM ubuntu:bionic

# LABEL about the custom image
LABEL maintainer="Salvador HM salvadorhm@gmail.com"
LABEL version="0.2"
LABEL description="This is a ubuntu:18.04 image with TensorFlow 1.14, python 3.6.9 and OpenCV 4.1.1.26"

# Definbe ENV files
ENV requirements /app/requirements.txt

# Copy requirements file
COPY requirements.txt ${requirements}

# Install packages
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get clean

# Install python packages
RUN pip3 install -r /app/requirements.txt
