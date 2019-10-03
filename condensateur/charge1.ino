/* test sur R=270 et C = 100 microF
 *  tau = 0,027 s
 */

unsigned long temps ; 
float charge ; 

void setup() 
	{
	// À COMPLÉTER : broche 7 = sortie
	//À COMPLÉTER : baudrate = 115200
	//À COMPLÉTER : passer la broche 7 à l'état bas
	//À COMPLÉTER : pendant 1 s (approx 50 tau) pour décharger le condo au cas où
	//À COMPLÉTER : affichage "temps;charge"
	}

void loop() 
	{
	if (Serial.available() != 0)
		{
		unsigned long t0 = micros() ; // date initiale
		//À COMPLÉTER : démarrage de la charge
      
		while (micros()-t0 <= 300000)// on limite à 300ms (tau=22ms)
			{
			temps = micros()-t0 ; //calcul de l'instant t
			// À COMPLÉTER : charge = valeur analogique lue sur A0
			// À COMPLÉTER : charge exprimée en % du maximum (1023)
			//À COMPLÉTER : affichage données "temps;charge"    
			}
		Serial.read() ;//on vide le buffer
		}
	}
