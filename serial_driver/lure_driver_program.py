#!/usr/bin/env python3
import sys
import driver_app as app

com_port = '/dev/cu.usbmodem32513201'
baud_rate = 115200 #update?
csv_file = sys.argv[1]
cal_file = 'calibration.csv'

controller = app.MissionController(com_port=com_port, baud_rate=baud_rate, csv_file=csv_file, calibration_file=cal_file, debug_commands=True, serial_listen=True)

controller.run()
