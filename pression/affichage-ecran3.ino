//MXP5500DP Capteur de pression 
// calcul et affichage de la pression moyenne
#include <Wire.h>
#include "rgb_lcd.h"

rgb_lcd lcd;
const float patm=101.3;// on définit la pression atmosphérique, valeur connue
const int cycles = 200; //nombre de mesures pour faire une moyenne
const int dur_mes = 1; //durée entre 2 mesures de la moyenne
const int dur_aff = 200; //durée entre 2 séries de mesure

int nombre_chevrons = 0 ; 
int p_min = 80 ; 
int p_max = 400 ;

void setup() {
  lcd.begin(16,2);
  Serial.begin(9600); //initialisation de ligne série
}

void loop(){
float resultatpression = 0.0 ;// on définit un float qui récupérera toutes les valeurs des pressions
for(int i = 0 ; i < cycles ; i++){ 
    float ana = analogRead(A0) ;   
    float pression_relat = ((ana / 1023.0)-0.04) /0.0018 ;  //utilise le modele determine par etalonnage
    float pression = pression_relat + patm;//calcul de la pression
    resultatpression += pression ;//on rajoute la valeur mesurée à la variable somme
    delay(dur_mes) ;
  } 

  resultatpression /= cycles ;          //calcul la moyenne des mesures
  Serial.print(resultatpression) ;      //affiche dans le moniteur serie les valeurs de pression en kPa
  Serial.println(" kPa") ;

  // gestion de l'affichage LCD
  lcd.clear();
  // affichage p = ...
  lcd.setCursor(0,0) ; 
  lcd.print("p = ");
  lcd.print(resultatpression);// Affiche la valeur sur le LCD. 
  lcd.print(" kPa");

  // calcul du nombre de chevrons à placer : 80 kPa : 0 chevron -- 400 kPa : 16 chevrons
  nombre_chevrons = 16*(resultatpression - p_min)/(p_max-p_min) ; 
  //affichage
  lcd.setCursor(0,1) ;
  for (int i = 1 ; i< nombre_chevrons+1 ; i++){
    lcd.print(">") ;
  }

  delay(dur_aff) ;                         // temps de latence entre 2 séries de mesures
}
