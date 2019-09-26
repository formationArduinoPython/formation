void setup() 
  {
  Serial.begin(9600);
  }

void loop() 
  {
  Serial.print(millis()) ;
  Serial.print(";") ;
  Serial.println(analogRead(A0)) ;
  delay(100);
  }
