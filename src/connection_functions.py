
import random
from device_conf import *
import calendar
import time

def get_timestamp():
    current_GMT = time.gmtime()

    time_stamp = calendar.timegm(current_GMT)
    # print("Current timestamp:", time_stamp)

    return time_stamp

def get_status_from_device(dev_id):
    
    batt        = round(BATTERY_PERC    + (random.random() * 15), ROUND_DECIMALS)
    temperature = round(TEMPERATURE_C   + (random.random() * 15), ROUND_DECIMALS)
    message     =  '{"id":' + str(dev_id) + ',"battery":' + str(batt) + ',"temperature":' + str(temperature) + '}'
    return      message

def get_status_from_edge(edge_id):
    
    batt        = round(BATTERY_PERC    + (random.random() * 15), ROUND_DECIMALS)
    temperature = round(TEMPERATURE_C   + (random.random() * 15), ROUND_DECIMALS)
    humidity    = round(HUMIDITY_PERC   + (random.random() * 20), ROUND_DECIMALS)
    pressure    = round(PRESSURE_KPa    + (random.random() * 50), ROUND_DECIMALS)
    message     =  '"edge_device":{"id":' + str(edge_id) + ',"battery":' + str(batt) + ',"temperature":' + str(temperature) + ',"humidity":' + str(humidity) + ',"pressure":' + str(pressure) + '}'

    return      message