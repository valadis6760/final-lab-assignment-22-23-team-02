
import random
import calendar
import time

def get_timestamp():
    current_GMT = time.gmtime()

    time_stamp = calendar.timegm(current_GMT)
    # print("Current timestamp:", time_stamp)

    return time_stamp

def get_random_value(init_value, range_value, min, max, decimals = 2, lower = False):

    base = init_value - range_value
    if not lower:
        range_value *= 2
    value = round(base   + (random.random() * (range_value))   , decimals)

    value = value if value < max else max
    value = value if value > min else min
    
    return value