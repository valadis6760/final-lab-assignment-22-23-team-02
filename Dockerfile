# Use an official Python runtime as a parent image
FROM ubuntu:latest

# Set the working directory to /app
# WORKDIR /app

# Copy the current directory contents into the container at /app
RUN mkdir /home/drone-app
ADD . /home/drone-app

# Install any needed packages specified in requirements.txt
# RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install -r ./requirements.txt

# # Make port 80 available to the world outside this container
# EXPOSE 80

# Define environment variable
ENV NAME jmad
ENV DRONE_APP_PATH /home/drone-app

# Run app.py when the container launches
CMD ["python3", "/home/drone-app/src/main.py"]
