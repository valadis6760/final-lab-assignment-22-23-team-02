# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
from azure.iot.device import IoTHubDeviceClient
from connection_functions   import get_status_from_edge

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table

class edge_device_client:

    def __init__(self,name, connection_str) -> None:
        self.name = name
        self.conn_str = connection_str
        self.devices = []
        pass

    def connect(self):
        self.client = IoTHubDeviceClient.create_from_connection_string(self.conn_str)

    def send_msg(self,str):
        self.client.send_message(str)
        
    def include_device(self, dev):
        self.devices.append(dev)

    def send_complete_status(self):

        message = '{' + get_status_from_edge(self.name) + ',"devices":['
        i = 0
        len_dev = len(self.devices)

        for dev in self.devices:
            message += dev.get_status() 
            if i < len_dev - 1:
                message += ','
            i += 1
            
        message += "]}"

        print( "Sending message: {}".format(message) )
        print ( "Message successfully sent" )
        self.client.send_message(message)