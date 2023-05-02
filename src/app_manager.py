# configuration

from azure_config import *
from device_conf import *
from azure_edge_device import edge_device_client
from device_simulator  import device_simulator
from system_functions import *

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import time
import enum

class app_type(enum.Enum):
    APP_CONTINIUS   = 0
    APP_FIXED       = 1

class app_manager():

    def __init__(self) -> None:
        print("\n\n---------------------------- INIT PYTHON APP ----------------------------\n\n")
        print ( "IoT Hub - Simulated device" )
        print ( "Press Ctrl-C to exit" )
        
    def check_init(self) -> None:

        # check if there are enough arguments, the app just accepts 1 argumment 
        args        = checkArguments(1)
        self.app_t   = app_type.APP_CONTINIUS
        
        if len(args) == 0:
            print("No argument passed ... exit: use --help")
            return False
        else:
            command     = args[0]
            if(command == "--help"):
                print('''
                EXECUTION: pyhton3 main.py [OPTION]
                OPTION:
                    --help              print this help string
                    -c, --continius     continius execution 
                    -n, --number [n]    execute n times a sending of the information
                ''')
                return False
            elif(command == "-c" or command == "--continius"):
                print("--> Coninius execution selected")
                self.app_t   = app_type.APP_CONTINIUS
            elif((command == "-n" or command == "--number") and len(args) == 2):
                print("--> Fixed execution selected: " + args[1])
                try:
                    self.numbers = int(args[1])
                except:
                    print("Argument not supported... exit: use --help")
                    return False
                self.app_t   = app_type.APP_FIXED
            else:
                print("Argument not supported... exit: use --help")
                return False
        
            return True
    
    def basic_task(self):
        # check all sevices status and send the payload in JSON format
        self.client.send_complete_status()
        time.sleep(DEALY_SENT_SECONDS)

    def start(self):
        try: 
            # connect to the azure device 
            print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
            self.client = edge_device_client(1, IOT_EDGE_CONNECTION_STRING)
            self.client.connect()

            # creation of simulated devices
            for id in range(DEVICE_NUMBER):
                self.client.include_device(device_simulator(id))

            if self.app_t == app_type.APP_CONTINIUS:
            
                while True:
                    self.basic_task()

            elif self.app_t == app_type.APP_FIXED:
                for i in range(self.numbers):
                    self.basic_task()

        except:
            sys.exit("ERROR: IoTHubClient sample stopped, check the connection string") 
        
        print ( "IoT Hub application correctly executed... exit" )