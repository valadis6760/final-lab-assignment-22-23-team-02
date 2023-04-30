## PYTHON SIMULATOR

# Install below packages

- sudo pip3 install azure-iot-device
- sudo pip3 install azure-iot-hub
- sudo pip3 install iothub-service-client
- sudo pip3 install iothub-device-client

# Run below on Azure CLI

#### below to add extension
az extension add --name azure-cli-iot-ext

### Below to start device monitor to check incoming telemetry data
az iot hub monitor-events --hub-name YourIoTHubName --device-id MyPythonDevice

