//Servo servo;

int cmd_value = 511; //should initialize starting value to "stop" command

void setup() {
  //  servo.attach(servoPin);
  //  servo.writeMicroseconds(1500); // send "stop" signal to ESC. Also necessary to arm the ESC.

  Serial.begin(115200); //make sure baud rate in Serial monitor is set to value here.

  //  delay(7000); // delay to allow the ESC to recognize the stopped signal.
}

void loop() {

  //  int potVal = analogRead(potentiometerPin); // read input from potentiometer.
  if (new_cmd_available()) {
    read_cmd();
  }
  int pwmVal = map(cmd_value, 0, 1023, 1100, 1900); // maps potentiometer values to PWM value.

  //  servo.writeMicroseconds(pwmVal); // Send signal to ESC.
}

bool new_cmd_available() {
  return (Serial.available() > 0);
}
void read_cmd() {
    int cmd = Serial.parseInt();
  //int cmd = 250;
  clear_Serial_buffer();

  if (check_cmd_validity(cmd)) {
    Serial.print("Received valid command: ");
    Serial.print(cmd);
    Serial.println(", updating motor.");
    cmd_value = cmd;
  }
  else {
    Serial.print("Interpreted input as invalid command: ");
    Serial.print(cmd);
    Serial.println(", not updating motor.");
  }
}

bool check_cmd_validity(int cmd) {
  return (cmd >= 0 && cmd <= 1023);
}

void clear_Serial_buffer() {
  while (new_cmd_available()) {
    Serial.read();
  }
}
