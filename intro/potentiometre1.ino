void setup() 
  {
  Serial.begin(9600);
  }

void loop() 
  {
  Serial.print("valeur analogique : ");
  Serial.println(analogRead(A0));
  delay(100);
  }
