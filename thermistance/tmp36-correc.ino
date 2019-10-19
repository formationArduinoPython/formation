// ce programme va permettre de lire la température sur le moniteur série

const float Ualim = 5.0 ; // tension d'alimentation du capteur à modifier le cas échéant

void setup(){
pinMode(A0, INPUT) ;//la broche analogique A0 est une entrée
Serial.begin(9600) ;//la vitesse de communication avec le port série est fixée à 9600 bits/s
}


void loop(){
float valeurAnaTMP36 = analogRead(A0) ;//la valeur ue par le CAN A0 est placée dans une variable
float tensionA0 = valeurAnaTMP36*Ualim/1023 ;
float temperature = (tensionA0-0.5)*100;

// on affiche la température
Serial.println(temperature) ;
delay(1000) ; //temps d'attente en ms entre 2 acquisitions
}
