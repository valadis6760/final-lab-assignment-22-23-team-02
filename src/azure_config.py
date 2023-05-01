# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table

IOT_EDGE_CONNECTION_STRING = "HostName=myIoTHubTutorialLucia.azure-devices.net;DeviceId=edgeDrone1;SharedAccessKey=g4tN5Hx96OVJt0A1y0H6inFz6nkS9p2cy+m2i248Gc8="
# IOT_EDGE_CONNECTION_STRING = "HostName=iot-hub-test-jmad.azure-devices.net;DeviceId=edgeDrone1;SharedAccessKey=9/BbwxMEgBySDiikroFeKtHwHrgVZ6eQ9J8o12mAzjo="

EDGE_DEVICE_ID      = 0
DEALY_SENT_SECONDS  = 10