int blinkPin = 1;

void setup()
{
  pinMode(blinkPin, OUTPUT);
}

void loop()
{
  digitalWrite(blinkPin, HIGH);
  delay(6000);
  digitalWrite(blinkPin, LOW);
  delay(1000);
}
