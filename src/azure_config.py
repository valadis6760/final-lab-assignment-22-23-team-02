# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table

# IOT_EDGE_CONNECTION_STRING = "HostName=iot-hub-cow-livestock.azure-devices.net;DeviceId=edge-drone-1;SharedAccessKey=XWi+RZhGqEEWV7XcFKjS3chZI651BVqbxzGuA6i19Zk="
IOT_EDGE_CONNECTION_STRING = "HostName=iot-hub-test-jmad.azure-devices.net;DeviceId=edgeDrone1;SharedAccessKey=9/BbwxMEgBySDiikroFeKtHwHrgVZ6eQ9J8o12mAzjo="

EDGE_DEVICE_ID      = 0
DEALY_SENT_SECONDS  = 5