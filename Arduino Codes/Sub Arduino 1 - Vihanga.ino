#include <MD_LM335A.h>

LM335A Temp(A1);
const int FanPin = 12; // Change to a different pin (12) for the motor fan
bool onSignalReceived = false; 

void setup() {
  Serial.begin(9600);
  pinMode(FanPin, OUTPUT);
}

void loop() {
  Temp.Read();
  int temperature = Temp.dC / 100.0 - 7.0;
  
  Serial.print("T:");
  Serial.println(temperature);

  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == '1') {
      onSignalReceived = true;
    } else if (command == '0') {
      onSignalReceived = false; 
    }
  }

  if (onSignalReceived) {
    digitalWrite(FanPin, HIGH); // Turn the fan on
  } else {
    if (temperature > 20) {
      digitalWrite(FanPin, HIGH); // Turn the fan on
    } else {
      digitalWrite(FanPin, LOW);  // Turn the fan off
    }
  }

  delay(1000);
}
