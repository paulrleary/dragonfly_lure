from .utilities.csv_reader import MissionCSVReader, CalibrationCSVReader, velocity_2_motor
from .utilities.serial_driver import SerialDriver

from time import time

class MissionController:
    def __init__(self, com_port = None, baud_rate = 9600, csv_file=None, calibration_file = None, debug_commands = False, serial_listen=False):
        self.start_time = time()
        self.serial = SerialDriver(port=com_port, baud_rate=baud_rate)
        self.serial_listen = serial_listen
        self.debug_commands = debug_commands
        calibration_df = CalibrationCSVReader(calibration_file).cal_df
        self.commands = velocity_2_motor(MissionCSVReader(csv_file), calibration_df)
        self.next_velocity_command = self.get_next_command()
        self.end_of_mission = False

    def __repr__(self):
        return 'Dragonfly lure controller, running {} on com port {} with baud rate {}'.format(self.commands.csv_file, self.serial.port, self.serial.baud_rate)

    def __str__(self):
        return self.__repr__()

    def run(self):
        # wait for next command time
        while not self.end_of_mission:
            if (time() - self.start_time) >= self.next_velocity_command.time:
                if self.debug_commands:
                    print('System time: {}, Issuing command: time {}. velocity {}, motor {}'.format(time() - self.start_time, *self.next_velocity_command))
                self.serial.write_serial(self.next_velocity_command.motor)
                self.next_velocity_command = self.get_next_command()
            if self.serial_listen:
                if self.serial.new_message():
                    print('Received response: {}'.format(self.serial.read_message()))


    def get_next_command(self):
        try:
            return next(self.commands)
        except StopIteration:
            self.end_of_mission = True




