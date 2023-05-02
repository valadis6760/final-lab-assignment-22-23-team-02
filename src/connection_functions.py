
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
    
    batt        = round(MIN_BATTERY_PERC    + (random.random() * (MAX_BATTERY_PERC  - MIN_BATTERY_PERC))    , ROUND_DECIMALS)
    temperature = round(MIN_TEMPERATURE_C   + (random.random() * (MAX_TEMPERATURE_C - MIN_TEMPERATURE_C))   , ROUND_DECIMALS)
    message     =  '{"id":' + str(dev_id) + ',"battery":' + str(batt) + ',"temperature":' + str(temperature) + '}'
    return      message

def get_status_from_edge(edge_id):
    
    batt        = round(MIN_BATTERY_PERC    + (random.random() * (MAX_BATTERY_PERC  - MIN_BATTERY_PERC)),   ROUND_DECIMALS)
    temperature = round(MIN_TEMPERATURE_C   + (random.random() * (MAX_TEMPERATURE_C - MIN_TEMPERATURE_C)),  ROUND_DECIMALS)
    humidity    = round(MIN_HUMIDITY_PERC   + (random.random() * (MAX_HUMIDITY_PERC - MIN_HUMIDITY_PERC)),  ROUND_DECIMALS)
    pressure    = round(MIN_PRESSURE_KPa    + (random.random() * (MAX_PRESSURE_KPa  - MIN_PRESSURE_KPa)),   ROUND_DECIMALS)
    message     =  '"edge_device":{"id":' + str(edge_id) + ',"battery":' + str(batt) + ',"temperature":' + str(temperature) + ',"humidity":' + str(humidity) + ',"pressure":' + str(pressure) + '}'

    return      message