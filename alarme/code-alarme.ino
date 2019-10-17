/*
 * un buzzer (alarme sonore) ou une LED (alarme lumineuse) est relié sur la sortie numérique 3
 * on reprend le montage du pont diviseur de l'activité précédente
 * on envoie la tension aux bornes de la photorésistance sur l'entrée 7
 */

const int alarme = 3 ; 
const int photo = 7 ; 
boolean etat ; 

void setup(){
  pinMode(alarme, OUTPUT) ;
  pinMode(photo, INPUT) ;
}

void loop()
  {
  etat = digitalRead(photo) ; // on prend la tension aux bornes de la photorésistance (env. 5 ou 0 V.)
  if (etat == 1)// si ça fait env. 5V = photoR non éclairée
    {
      digitalWrite(alarme, HIGH) ; // on déclenche l'alarme
      delay(2000) ;  // pendant 2 secondes
    }
  else//sinon
    {
      digitalWrite(alarme, LOW) ;// pas d'alarme 
    }
  }
