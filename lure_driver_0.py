import serial #not part of library in new venv??
import time

# com_port = 'COM4'
com_port = '/dev/cu.usbmodem32513201'
baud = 9600
arduino = serial.Serial(port=com_port, baudrate=baud, timeout=.5)




def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(1)
    data = arduino.readline()
    return data

while True:
    num = input("Enter a number: ") # Taking input from user
    value = write_read(num)
    print(value) # printing the value