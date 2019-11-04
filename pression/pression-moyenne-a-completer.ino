//MXP5500DP Capteur de pression 
// calcul de la pression moyenne

const float patm=101.3;// on définit la pression atmosphérique, valeur connue
const int cycles = 200; //nombre de mesures pour faire une moyenne
const int dur_mes = 1; //durée entre 2 mesures pour calcul de la moyenne
const int dur_aff = 200; //durée entre 2 séries de mesure

void setup() {
  Serial.begin(9600); //initialisation de ligne série
}

void loop(){
float resultatpression = 0.0 ;// on définit un float qui récupérera toutes les valeurs des pressions
for(int i = 0 ; i < cycles ; i++){ //BLOC À COMPLÉTER : acquisition des valeurs pour calcul de moyenne
									// À COMPLÉTER  
									// À COMPLÉTER  
									// À COMPLÉTER  
									// À COMPLÉTER  
    delay(dur_mes) ;		// durée entre 2 acquisitions
  } 

										//À COMPLÉTER : calcule la moyenne des mesures
										//À COMPLÉTER : affiche dans le moniteur serie les valeurs de pression en kPa
										
  delay(dur_aff) ;                         // temps de latence entre 2 séries de mesures
}
