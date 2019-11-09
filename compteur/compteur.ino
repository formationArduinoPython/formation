int capteur = 3 ; //capteur placé sur l'entrée numérique 3
boolean memoire ; // mémoire de l'ancien état du capteur
unsigned long temps ; // interv. de temps écoulé depuis le démarrage
unsigned long delta_t ; // interv. de temps pour un tour de roue

void setup() {
Serial.begin(9600) ; 
pinMode(capteur, INPUT) ; 
}

void loop() {
boolean etat = digitalRead(capteur) ; 
if ((etat == 1) && (etat != memoire))
    {
    delta_t = millis() - temps ; 
    temps = millis() ;
    Serial.print(delta_t) ;Serial.println(" ms");   
    delay(1) ; 
    }
memoire = etat ; 
}
