# Using the Python Device SDK for IoT Hub:
#   https://github.com/Azure/azure-iot-sdk-python
# The sample connects to a device-specific MQTT endpoint on your IoT Hub.
import azure
from azure.iot.device import IoTHubDeviceClient
from connection_functions   import get_random_value, get_timestamp
from device_conf import *

# The device connection string to authenticate the device with your IoT hub.
# Using the Azure CLI:
# az iot hub device-identity show-connection-string --hub-name {YourIoTHubName} --device-id MyNodeDevice --output table

class edge_device_client:

    def __init__(self,name, connection_str, variance) -> None:
        self.name           = name
        self.conn_str       = connection_str
        self.devices        = []
        self.temperature    = get_random_value(INIT_TEMPERATURE_C, TEMPERATURE_VARIANCE, MIN_TEMPERATURE_C, MAX_TEMPERATURE_C)
        self.battery        = get_random_value(INIT_BATTERY_PERC, BATTERY_PERC_VARIANCE, MIN_BATTERY_PERC, MAX_BATTERY_PERC, lower=True)
        self.humidity       = get_random_value(INIT_HUMIDITY_PERC, HUMIDITY_PERC_VARIANCE, MIN_HUMIDITY_PERC, MAX_HUMIDITY_PERC)
        self.pressure       = get_random_value(INIT_PRESSURE_KPa, PRESSURE_KPa_VARIANCE, MIN_PRESSURE_KPa, MAX_PRESSURE_KPa)
        pass

    def connect(self):
        self.client = IoTHubDeviceClient.create_from_connection_string(self.conn_str)

    def send_msg(self,str):
        self.client.send_message(str)
        
    def include_device(self, dev):
        self.devices.append(dev)

    def send_complete_status(self):

        self.temperature    = get_random_value(self.temperature, TEMPERATURE_VARIANCE, MIN_TEMPERATURE_C, MAX_TEMPERATURE_C)
        self.battery        = get_random_value(self.battery, BATTERY_PERC_VARIANCE, MIN_BATTERY_PERC, MAX_BATTERY_PERC)
        self.humidity       = get_random_value(self.humidity, HUMIDITY_PERC_VARIANCE, MIN_HUMIDITY_PERC, MAX_HUMIDITY_PERC)
        self.pressure       = get_random_value(self.pressure, PRESSURE_KPa_VARIANCE, MIN_PRESSURE_KPa, MAX_PRESSURE_KPa)

        edge_dev_info = '"edge_device":{"id":' + str(self.name) + ',"battery":' + str(self.battery) + ',"temperature":' + str(self.temperature) + ',"humidity":' + str(self.humidity) + ',"pressure":' + str(self.pressure) + '}'

        message = '{"ts":'+ str(get_timestamp()) + ',' + edge_dev_info + ',"devices":['
        i = 0
        len_dev = len(self.devices)

        for dev in self.devices:
            dev.get_status() # update values
            message += '{"id":' + str(dev.id) + ',"battery":' + str(dev.battery) + ',"temperature":' + str(dev.temperature) + '}'
            if i < len_dev - 1:
                message += ','
            i += 1
            
        message += "]}"

        print( "Sending message: {}".format(message) )

        try:
            self.client.send_message(message)
            print ( "Message successfully sent" )
        except azure.iot.device.exceptions.CredentialError:
            return False
        
        return True