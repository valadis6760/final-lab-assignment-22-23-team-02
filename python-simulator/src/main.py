# configuration

from azure_config import *
from device_conf import *
from azure_edge_device import edge_device_client
from device_simulator  import device_simulator

# Copyright (c) Microsoft. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for full license information.

import time

if __name__ == '__main__':
    print ( "IoT Hub - Simulated device" )
    print ( "Press Ctrl-C to exit" )

    try:
        
        # connect to the azure device 
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )
        client = edge_device_client("drone_1", IOT_EDGE_CONNECTION_STRING)
        client.connect()

        # creation of simulated devices
        for id in range(DEVICE_NUMBER):
            client.include_device(device_simulator(id))
          
        while True:
            # Send the message

            client.send_complete_status()
            
            time.sleep(3)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )