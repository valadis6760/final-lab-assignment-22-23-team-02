# PYTHON SIMULATOR

## Install below packages

- sudo pip3 install azure-iot-device
- sudo pip3 install azure-iot-hub
- sudo pip3 install iothub-service-client
- sudo pip3 install iothub-device-client

## Basic test on Azure CLI

#### below to add extension
az extension add --name azure-cli-iot-ext

### Below to start device monitor to check incoming telemetry data
az iot hub monitor-events --hub-name YourIoTHubName --device-id MyPythonDevice

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/Ytkh1eeE)

