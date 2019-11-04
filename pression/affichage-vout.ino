// affichage de la tension Vout du capteur de pression

void setup(){
Serial.begin(9600) ;//initialisation de ligne série
}

void loop(){
int ana = analogRead(A0) ;//variable entière ana contient le résultat du CAN de A0
float tension = ana*5.0/1023.0 ;//variable décimale contient la valeur Vout

Serial.println(tension); // affichage de la valeur de la tension Vout avec un retour ligne

delay(100) ;// délais de 100 ms pour refaire un nouveau cycle
}
