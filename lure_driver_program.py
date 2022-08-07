# import serial #not part of library in new venv??
# import time
#
# # com_port = 'COM4'
# com_port = '/dev/cu.usbmodem32513201'
# baud = 9600
# # arduino = serial.Serial(port=com_port, baudrate=baud, timeout=.5)
#
# # need class to manage commands and timing variables
# class SerialDriver:
#     def __init__(self, ser = serial.Serial(port=com_port, baudrate=baud, timeout=.5), timeout=1):
#         self.ser = ser
#         self.start_time = time.time()
#         self.timeout = timeout
#         self.response_data = b''
#
#     def write_serial(self, x):
#         msg = str(x)
#         self.ser.write(bytes(msg, 'utf-8'))
#
#     def new_message(self):
#         response = self.ser.readline()
#         if response:
#             self.response_data = response
#             return True
#         else:
#             return False
#
#     def read_message(self):
#         message = self.response_data
#         self.response_data = b''
#         return message

# import csv
# class MissionCSVReader:
#     def __init__(self, csv_file):
#         pass

# arduino = SerialDriver()
#
# start = time.time()
#
# times = [3, 5, 7, 9]
# speeds = [100, 200, 300, 400]
#
# for i in range(0, len(times)):
#     if (time.time() - start) < times[i]:
#         arduino.write_serial(speeds[i])
#
#     while((time.time() - start) < times[i]):
#         if arduino.new_message():
#             print(arduino.read_message())

import sys
import driver_app as app

com_port = '/dev/cu.usbmodem32513201'
baud_rate = 115200 #update?
csv_file = sys.argv[1]
cal_file = 'calibration.csv'

controller = app.MissionController(com_port=com_port, baud_rate=baud_rate, csv_file=csv_file, calibration_file=cal_file, debug_commands=True, serial_listen=True)

controller.run()


    # print(value) # printing the value