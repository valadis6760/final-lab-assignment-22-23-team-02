
from connection_functions   import get_status_from_device

class device_simulator:

    def __init__(self, id) -> None:
        self.id = id
        pass

    def get_status(self):

        return get_status_from_device(self.id)


    