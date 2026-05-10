#include <Arduino.h>
const int buttonPin = 2;
int lastButtonState = HIGH;

void setup() {
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(9600);
}

void loop() {
  int buttonState = digitalRead(buttonPin);

  if (lastButtonState == HIGH && buttonState == LOW) {
    Serial.println("idea");
    delay(200);
  }

  lastButtonState = buttonState;
}
