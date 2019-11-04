#include <rgb_lcd.h>

//lecture de l'entrée analogique

void setup(){
Serial.begin(9600) ;//initialisation de ligne série
}

void loop(){
int ana = analogRead(A0) ;//variable entière ana contient le résultat du CAN de A0

Serial.println(ana);// affichage de la valeur de la variable avec un retour ligne

delay(100) ;// délais de 100 ms pour refaire un nouveau cycle
}
