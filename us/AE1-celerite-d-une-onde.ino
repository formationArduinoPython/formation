const byte TRIGGER_PIN = 2; // Broche TRIGGER
const byte ECHO_PIN = 3;    // Broche ECHO
 /* Constantes pour la fonction pulseIn */
const unsigned long DUREE_SORTIE = 25000; // 25ms = ~8m à 340m/s
/* Célérité du son dans l'air en m/s */
const float TEMPERATURE = 20 ; 

void setup() {
/* Initialise le port série */
  Serial.begin(9600);
     /* Initialise les broches */
  pinMode(TRIGGER_PIN, OUTPUT);
  digitalWrite(TRIGGER_PIN, LOW); // La broche TRIGGER doit être à LOW au repos
  pinMode(ECHO_PIN, INPUT);
}
void loop() {
/* 1. Calcule la célérité du son en fonction de la température de la pièce:*/
  float CELERITE =   ;// A COMPLETER

 
/* 2. Lance une mesure de distance en envoyant une impulsion HIGH de 10µs sur la broche TRIGGER */
  digitalWrite(TRIGGER_PIN, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIGGER_PIN, LOW);

  
/* 3. Mesure le temps entre l'envoi de l'impulsion ultrasonique et son écho (si il existe). 
  Renvoie 0 si aucune implusion n'a été détectée avant la durée DUREE_SORTIE  */
  long temps_mesure = pulseIn(ECHO_PIN, HIGH, DUREE_SORTIE); //
  
  
/* 4. Calcul la distance à partir du temps mesuré */
  float distance_m =   ;  // A COMPLETER

   
/* 5. Affiche les résultats de la mesure de la durée et du calcul de la distance avec 3 décimales */
  Serial.print("temps mesuré : ");
  Serial.println(temps_mesure);
  Serial.print("Distance: ");
  Serial.println(distance_m,3);

  
/* 6. Délai d'attente de 2 secondes pour éviter d'afficher trop de résultats à la seconde */
  delay(2000);
}

