// affichage pression abolue

const float patm=101.3;// on définit la pression atmosphérique, valeur connue

void setup(){
Serial.begin(9600) ;//initialisation du port série
}

void loop(){
int ana = analogRead(A0) ;//variable entière ana contient le résultat du CAN de A0

float delta_p = ((ana / 1023.0)-0.04) /0.0018 ;  //utilise le modele determine par etalonnage
float pression = delta_p + patm;//calcul de la pression

Serial.print(pression); // affichage de la valeur de "pression" avec un retour ligne
Serial.println(" kpa");
delay(100) ;// délais de 100 ms pour refaire un nouveau cycle
}
