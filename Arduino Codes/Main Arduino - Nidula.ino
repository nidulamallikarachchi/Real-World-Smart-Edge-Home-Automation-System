// Define the pin connections
const int potPin = A0;  // Potentiometer connected to A0
const int ledPin = 4;   // LED connected to pin 4

// Define a threshold value to determine darkness
const int threshold = 500;

bool onSignalReceived = false; // Added declaration of the variable

void setup() {
  // Initialize the serial communication for debugging
  Serial.begin(9600);
  
  // Set the LED pin as an output
  pinMode(ledPin, OUTPUT);
}

void loop() {
  // Read the value from the potentiometer (light sensor)
  int sensorValue = analogRead(potPin);
  
  // Print the sensor value to the Serial Monitor in the form of "L:{value}"
  Serial.print("L:");
  Serial.println(sensorValue);

  if(Serial.available() > 0){
    char command = Serial.read();
    if(command == '1'){
      onSignalReceived = true; 
    } else if (command == '0') {
      onSignalReceived = false; 
    }
  }

  if(onSignalReceived == true){
    digitalWrite(ledPin, HIGH);
  } else {
    // Check if the sensor value is below the threshold (indicating darkness)
    if (sensorValue < threshold) {
      // Turn on the LED
      digitalWrite(ledPin, HIGH);
    } else {
      // Turn off the LED
      digitalWrite(ledPin, LOW);
    }
  }

  delay(1000);
}
