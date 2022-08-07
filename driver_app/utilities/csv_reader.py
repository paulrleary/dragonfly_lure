import csv
# from time import time

from collections import namedtuple
import numpy as np

class MissionCSVReader:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        return self.parse_csv(self.csv_file)

    def parse_csv(self, csv_file):
        VelocityCommand = namedtuple('VelocityCommand', 'time, velocity')
        with open(csv_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            header_line = next(csv_reader)

            commands = [
                VelocityCommand(*np.asarray(line).astype(float))
                for line in csv_reader
                if len(line)==2
            ]

            self.commands = iter(commands)

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.commands)

import pandas
class CalibrationCSVReader:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.cal_df = self.parse_csv(self.csv_file)

    def parse_csv(self, csv_file):
        return pandas.read_csv(csv_file)

MotorCommand = namedtuple('MotorCommand', 'time, velocity, motor')
def convert_command(velocity_command, cal_df):
    velocity = velocity_command.velocity
    d = cal_df[(cal_df['vel_min'] <= velocity) & (cal_df['vel_max'] > velocity)].values[0]
    m = (d[3] - d[2]) / (d[1] - d[0])
    b = d[2] - m*d[0]
    motor = round(m*velocity + b)

    if (motor - b) == 0:
        new_velocity = 0
    else:
        new_velocity = (motor - b)/m #new_velocity is the true velocity after discretization
    return MotorCommand(velocity_command.time, new_velocity, motor)

def velocity_2_motor(velocity_command_iterator, cal_df):
    return iter([
        convert_command(command, cal_df)
        for command in velocity_command_iterator
    ])

