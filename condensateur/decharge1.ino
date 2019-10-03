unsigned long temps ; 
float charge ; 
float R = 270 ;
float C = 100*pow(10, -6) ;  
float tau = R*C*1e6 ;//constante de temps en us

void setup() 
  {
  pinMode(7, OUTPUT) ;
  Serial.begin(115200) ; 
  digitalWrite(7, HIGH) ;
  delayMicroseconds(10*tau) ;
  Serial.println("temps;charge") ; 
  }

void loop() 
{
  //démarrage d'une charge par envoi donnée sur port série
  if (Serial.available() != 0)
    {
      unsigned long t0 = micros() ;
      digitalWrite(7, LOW) ;
      while (micros()-t0 <= 10*tau)
        {
        temps = micros()-t0 ; 
        charge = analogRead(A0) ; 
        charge = charge*100.0/1023.0 ; 
        Serial.print(temps) ; Serial.print(";") ; Serial.println(charge) ;    
        }
     Serial.read() ;//on vide le buffer
    }
}
