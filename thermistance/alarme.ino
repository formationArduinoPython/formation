/* 
 * ce programme va permettre de déclencher une alarme
 * en fonction de Requiv donc de la température
 * pas d'affichage de température ni de Requiv, juste info visuelle
 * par LEDR ou LEDV sur la température
 * (on pourra rajouter un affichage de Requiv par exemple)
 */

const int R0 = 1000 ; 
const int Rlim = 115 ; // valeur minimale pour infusion
const int LEDR = 3 ; 
const int LEDV = 7 ; 

void setup()
  {
  pinMode(LEDR, OUTPUT) ; 
  pinMode(LEDV, OUTPUT) ; 
  pinMode(A2, INPUT) ; 
  }


void loop()
	{
    // acquisition de Réquivalente
    float valeurAnaRequiv = analogRead(A2) ; 
    float Requiv = R0 * valeurAnaRequiv/(1024.0-valeurAnaRequiv) ;

	if (Requiv <= Rlim)// T >= 70 : alarme rouge
		{
		digitalWrite(LEDR, HIGH) ; 
		digitalWrite(LEDV, LOW) ; 
		}
	else // T < 70 : alarme verte
		{
		digitalWrite(LEDV, HIGH) ; 
		digitalWrite(LEDR, LOW) ;
		}

	delay(1000) ; 

	}
