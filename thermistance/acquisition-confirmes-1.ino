/* 
 * ce programme va permettre de lire température et Réquivalente 
 * sur moniteur série en continu
 */

const float Ualim = 5.0 ; 
const int R0 = 1000 ; 

void setup()
	{
	pinMode(A0, INPUT) ;// A0 pour TMP36
	pinMode(A2, INPUT) ; // A2 pour div de tension CTN
	Serial.begin(9600) ;// vitesse de communication
	}


void loop()
	{
	// acquisition de la température
	float valeurAnaTMP36 = analogRead(A0) ;// 
	float tensionA0 = valeurAnaTMP36*Ualim/1023 ;
	float temperature = (tensionA0-0.5)*100;

	// acquisition de Réquivalente
	float valeurAnaUequiv = analogRead(A2) ;
	float Uequiv = valeurAnaUequiv*Ualim/1023.0 ; 
	float Requiv = R0*Uequiv/(Ualim-Uequiv) ;

	// on affiche le couple température ; Requiv
	Serial.print(temperature) ; Serial.print(";") ; Serial.println(Requiv) ; 
	delay(5000) ; //
	}
