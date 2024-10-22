#include <MD_LM335A.h>

const int motorPin = 12;          // Pin connected to the motor
const int sensorPin = A0;         // Pin connected to the soil moisture sensor
const int moistureThreshold = 1000; // Threshold for soil moisture level (adjust as needed)
bool onSignalReceived = false;

void setup() {
  pinMode(motorPin, OUTPUT);      // Set motor pin as an output
  pinMode(sensorPin, INPUT);      // Set sensor pin as an input
  Serial.begin(9600);             // Initialize serial communication at 9600 bps
}

void loop() {

  int moistureLevel = analogRead(sensorPin); // Read the soil moisture level
  Serial.print("M:");
  Serial.println(moistureLevel);   // Output the moisture level to the serial monitor

  if(Serial.available() > 0){
    char command = Serial.read();
    if(command == '1'){
      onSignalReceived = true;
    }else if (command == '0'){
      onSignalReceived = false; 
    }
  }

  if(onSignalReceived == true){
    digitalWrite(motorPin, HIGH);
  }else{
    if (moistureLevel < moistureThreshold) {
      digitalWrite(motorPin, HIGH); // Turn on the motor if moisture level is below threshold
    } else {
      digitalWrite(motorPin, LOW);  // Turn off the motor if moisture level is above threshold
    }
  }

  delay(1000); // Wait for 1 second before taking the next reading
}
