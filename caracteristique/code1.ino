void setup() {                        // phase lue une seule fois
  Serial.begin(9600) ;                // vitesse de communication
  Serial.println("# ValeurAna_Ug") ; // on écrit une phrase d'intro
}

void loop() {                         // phase lue en boucle infinie
  int ValeurAna_Ug = analogRead(A0) ; //définition de ValeurAna_Ug
  Serial.println(ValeurAna_Ug) ;     // on l'affiche sur le moniteur série
  delay(200) ;   
}