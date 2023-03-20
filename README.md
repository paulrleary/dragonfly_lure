
# dragonfly_lure repository:

##First time setup:
I recommend setting up a python virtual environment to run this code. To do this, in the terminal, navigate to whichever folder you wish to contain your main functions. The command to create the environment is:
python3 -m venv *name_of_your_environment*

commonly run as:
python3 -m venv .venv

To use your environment, you must activate it:
source .venv/bin/activate

to deactivate the environment simply run: deactivate

With your environment activated, from the serial_driver folder, run:
pip install -r requirements.txt


# dragonfly_lure

potentiometer_test0 should theoretically be the code you have already been using.  It's possible I did extra something previously to ensure that the middle knob position reliably made the motor stop.  If the middle position is now finicky, we can fix.

serial_test0 is the new code which should allow you to control the motor speed from the Arduino serial monitor.  Make sure to set the baud rate to 9600.  We can update this rate as needed.  If it works as intended, you should be able to type in a number between 0 and 1023 where 0 is full speed backwards, and 1023 is full speed forward, and 511 should be stopped.  I think my feedback printing should be sufficient for troubleshooting.  Other characters, or things not interpreted as a valid value should not affect the motor.  This should suffice for putting together a motor calibration, and allow us to move forward with something more finalized.

