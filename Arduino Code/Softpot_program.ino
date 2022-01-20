#define BAUDRATE        115200
int softpotPin = A0; //analog pin 0

void setup(){
digitalWrite(softpotPin, HIGH); //enable pullup resistor
Serial.begin(BAUDRATE); // Frequency at which we communicate with serial for printing
}

void loop(){
int softpotReading = analogRead(softpotPin);

Serial.println(softpotReading);
delay(250); //just here to slow down the output for easier reading
}
