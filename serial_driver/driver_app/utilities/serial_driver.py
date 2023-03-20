import serial #not part of library in new venv??
import time

# com_port = 'COM4'
com_port = '/dev/cu.usbserial-A90837S1'
# com_port = '/dev/cu.usbmodem32513201' #update to system?

baud = 115200
# arduino = serial.Serial(port=com_port, baudrate=baud, timeout=.5)

# need class to manage commands and timing variables
class SerialDriver:
    def __init__(self, port=com_port, baud_rate=baud, timeout=1):
        self.port = port
        self.baud_rate = baud_rate
        self.timeout = timeout
        self.serial = serial.Serial(port=self.port, baudrate=self.baud_rate, timeout=self.timeout)
        self.start_time = time.time()
        self.timeout = timeout
        self.response_data = b''

    def write_serial(self, x):
        # msg = str(x)
        msg = str(x) + ';' #workaround for Arduino's Serial.parseInt() slowness issue when it only receives an integer and not other chars
        self.serial.write(bytes(msg, 'utf-8'))

    def new_message(self):
        response = self.serial.readline()
        if response:
            self.response_data = response
            return True
        else:
            return False

    def read_message(self):
        message = self.response_data
        self.response_data = b''
        return message