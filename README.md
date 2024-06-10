# Object Detection in Images Using Transformers

## Description

This project is dedicated to the development of a back-end application in Python for object detection in images (ex Bank Docs) using transformer models via API. 
It also includes test cases to verify the performance and correctness of the model.

## Features

- Object detection in images using transformer models
- RESTful API to submit images and get detection results
- Error handling and input validation
- Unit and integration tests to ensure code quality

## Project Files
requirement.txt: This file lists the Python dependencies needed for the project.
Dockerfile : This file defines the Docker environment for the application.
app.py : This is the main application file.
test_with_pytest : This is the file containing the tests for the application.
Tabeldetector.py : This is the file containing the TableDetector class to detect object in Bank doc images.

## The user guide 
This user guide walks you through installing, using, and testing your object detection application using Docker
cmd for installing and building our customed docker image : docker build -t appimage .
cmd for runing the docker image : docker run appimage 
cmd for app testing : 
  docker run -it appimage /bin/bash
  python test_with_pytest.py

## Results

### input image 
![Screenshot](Bank-doc.jpg)
### output image 
![Screenshot](Api_result.jpg)

### teminal output  
#### using this cmd 
##### docker run appimage
![Screenshot](screen_shots/screenshot1.png)
### terminal pytest output
#### using this cmds
##### docker run -it appimage /bin/bash
##### python test_with_pytest.py
![Screenshot](screen_shots/screenshot2.png)
### terminal output (case of not existing image file)
![Screenshot](screen_shots/screnshot3.png)
