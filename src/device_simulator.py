
from connection_functions   import get_random_value
from device_conf import *

class device_simulator:

    def __init__(self, id, create_alamrs = False) -> None:
        self.id = id
        self.temperature    = get_random_value(INIT_TEMPERATURE_C, TEMPERATURE_VARIANCE, MIN_TEMPERATURE_C, MAX_TEMPERATURE_C)
        self.battery        = get_random_value(INIT_BATTERY_PERC, BATTERY_PERC_VARIANCE, MIN_BATTERY_PERC, MAX_BATTERY_PERC, lower=True)
        pass

    def get_status(self):

        self.temperature    = get_random_value(self.temperature, TEMPERATURE_VARIANCE, MIN_TEMPERATURE_C, MAX_TEMPERATURE_C)
        self.battery        = get_random_value(self.battery, BATTERY_PERC_VARIANCE, MIN_BATTERY_PERC, MAX_BATTERY_PERC)

        # return '{"id":' + str(self.id) + ',"battery":' + str(self.battery) + ',"temperature":' + str(self.temperature) + '}'


    