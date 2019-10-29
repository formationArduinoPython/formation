//déclaration des broches
const int piezo=0; //capteur piézoélectrique à la broche A0


//variables
int mesure_piezo; // valeur mesurée par le capteur piézoélectrique(entre 0 et 1023)


void setup() {
pinMode(piezo, INPUT); // définition de la borne A0 en entrée
Serial.begin(2000000); // l'onde est très rapide, il faut augmenter le débit binaire
}

void loop() {
mesure_piezo=analogRead(piezo);
Serial.println(mesure_piezo);

}
