/*
 * acquisitions pdt 300ms dès qu'on reçoit une donnée du port série
 * attention à ce que le temps d'acquisition python soit plus court que celui arduino (sinon il reste bloqué sur port série)
 * avec ce programme, on relancera une acquisition par reset sur carte puis compilation du fichier python
*/
unsigned long temps ; 
float charge ; 
unsigned long duree_acquisition_Arduino = 300000 ; 

void setup() 
  {
  pinMode(7, OUTPUT) ;
  Serial.begin(115200) ; 
  digitalWrite(7, LOW) ;
  delay(1000) ;
  }

void loop() 
  {
  //démarrage d'une charge par envoi donnée sur port série
  if (Serial.available() != 0)
    {
    unsigned long t0 = micros() ;
    digitalWrite(7, HIGH) ;
    while (micros()-t0 <= duree_acquisition_Arduino)
      {
      temps = micros()-t0 ; 
      charge = analogRead(A0)*100.0/1023.0 ;
      Serial.print(temps) ; Serial.print(";") ; Serial.println(charge) ;    
      }
    Serial.read() ;//on vide le buffer
    }
  }
