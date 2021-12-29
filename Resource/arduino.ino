
void setup() {
  Serial.begin(115200); // opens serial port, sets data rate to 9600 bps
}

void loop() {
  // check if data is available
  if (Serial.available() > 0) {
    // read the incoming string:
    String incomingString = Serial.readString();

    // prints the received data
    delay(1000);
//    Serial.print("I received: ");
//    Serial.println(incomingString);
    Serial.write("200");
  }
}