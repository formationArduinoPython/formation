//déclaration des broches
const int piezo1=0; //capteur piézoélectrique à la broche A0
const int piezo2=1; //capteur piézoélectrique à la broche A1


//variables
int mesure_piezo1; // valeur mesurée par le premier capteur piézoélectrique (entre 0 et 1023)
int mesure_piezo2; // valeur mesurée par le deuxième capteur piézoélectrique (entre 0 et 1023)
int ref_bruit;     // mesure du bruit ambiant
unsigned long temps0; //date du début de l'écoute en microseconde
unsigned long tempst; //temps courant en microseconde
unsigned long deltat; //intervalle de temps en microseconde
float vitesse;

void setup() {
pinMode(piezo1, INPUT); // définition de la borne A0 en entrée
pinMode(piezo2, INPUT); // définition de la borne A1 en entrée
Serial.begin(2000000); // l'onde est très rapide, il faut augmenter le débit binaire
}

void loop() {
// mesure du bruit
ref_bruit=analogRead(piezo1);
delay(2000);

//début des mesures
Serial.println("C'est parti, frappez le matériau");
mesure_piezo1=analogRead(piezo1);
mesure_piezo2=analogRead(piezo2);

//attente d'un signal autre que le bruit
while(mesure_piezo1<ref_bruit){
  mesure_piezo1=analogRead(piezo1);
  }
temps0=micros(); // mesure de t0, date à laquelle le front d'onde arrive sur le capteur 1

while(mesure_piezo2<ref_bruit){
  mesure_piezo2=analogRead(piezo2);
  }
tempst=micros(); // mesure de tf, date à laquelle le front d'onde arrive sur le capteur 2

deltat=tempst - temps0;   // calcul du retard

vitesse = 1E6/deltat ;    // calcul de la vitesse en m/s
Serial.print("valeur estimée de la vitesse en m/s :  ");
Serial.println(vitesse);


}
