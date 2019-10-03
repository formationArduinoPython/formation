/* test sur R=270 et C = 100 microF
 *  tau = 0,027 s
 */

unsigned long temps ; 
float charge ; 

void setup() 
	{
	pinMode(7, OUTPUT) ; // À COMPLÉTER : broche 7 = sortie
	Serial.begin(115200) ; //À COMPLÉTER : baudrate = 115200
	digitalWrite(7, LOW) ;//À COMPLÉTER : passer la broche 7 à l'état bas
	delay(1000) ;//À COMPLÉTER : pendant 1 s (approx 50 tau) pour décharger le condo au cas où
	Serial.println("temps;charge") ;  //À COMPLÉTER : affichage "temps;charge"
	}

void loop() 
	{
	//démarrage d'une charge par envoi donnée sur port série
	if (Serial.available() != 0)
		{
		unsigned long t0 = micros() ; // date initiale
		digitalWrite(7, HIGH) ; //À COMPLÉTER : démarrage de la charge
      
		while (micros()-t0 <= 300000)// on limite à 300ms (tau=22ms)
			{
			temps = micros()-t0 ; //calcul de l'instant t
			charge = analogRead(A0) ; // À COMPLÉTER : charge = valeur analogique lue sur A0
			charge = charge*100.0/1023.0 ; // À COMPLÉTER : charge exprimée en % du maximum (1023)
			Serial.print(temps) ; Serial.print(";") ; Serial.println(charge) ;//À COMPLÉTER : affichage données "temps;charge"    
			}
		Serial.read() ;//on vide le buffer
		}
	}
