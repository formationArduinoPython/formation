void setup() {                        // phase lue une seule fois
  Serial.begin(9600) ;                // vitesse de communication
  Serial.println("# ValeurAna_Ug;ValeurAna_Ur") ; // on écrit une phrase d'intro
  int compteur = 0 ;                  // on va faire 150 mesures, on initialise un compteur à zéro
  while (compteur <=150){             // tant qu'on n'a pas fait 150 mesures...
    int ValeurAna_Ug = analogRead(A0) ; //définition de ValeurAna_Ug
    int ValeurAna_Ur = analogRead(A1) ; //définition de ValeurAna_Ur
    Serial.print(ValeurAna_Ug) ;        // on affiche ValeurAna_Ug
    Serial.print(";") ;                 // on affiche un point-virgule     
    Serial.println(ValeurAna_Ur) ;// on affiche ValeurAna_Ur, on revient à la ligne
    compteur = compteur+1 ;       // on augmente le compteur de 1 et on recommence la boucle
    delay(100) ;                  // pause de 100 ms entre chaque acquisition
  }
  Serial.println("STOP") ;              // fin de l'acquisition des données
}

void loop() {// phase lue en boucle infinie
    
}