void setup() {
  // put your setup code here, to run once:
pinMode(13, INPUT) ; 
Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
boolean etat = digitalRead(13) ; 
Serial.println(etat) ; 
delay(100) ; 
}
