
import random
from device_conf import *

def get_status_from_device(dev_id):

    temperature = TEMPERATURE_C + (random.random() * 15)
    humidity    = HUMIDITY_PERC + (random.random() * 20)
    pressure    = PRESSURE_KPa  + (random.random() * 2)
    message     =  'device:{"id":' + str(dev_id) + ',"humidity":' + str(humidity) + ',"temperature":' + str(temperature) + ',"pressure":' + str(pressure) +'}'
    return message

def get_status_from_edge(edge_id):

    batt = BATTERY_PERC + (random.random() * 15)
    message   =  'edge_device:{"id":' + str(edge_id) + ',"battery":' + str(batt) + '}'
    return message