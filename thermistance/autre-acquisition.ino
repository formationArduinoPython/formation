// ce code va permettre de lire la température et Requiv sur le port série

const float Ualim = 5.0 ; 
const float R0 = 1000.0 ; 
float temperature = 100.0 ; 

void setup(){
pinMode(A0, INPUT) ; // la sortie du TMP36 est reliée à l'entrée A0 du microcontrôleur
pinMode(A2, INPUT) ; // le pont diviseur est relié à l'entrée A2 
 Serial.begin(9600) ; //on initialise le port série
}

void loop()
{
while (temperature > 30)
  {
  float sommeTemperature = 0 ; float sommeRequiv = 0 ; 
  
  for (int i = 1 ; i <=20 ; i++)
    {
    float valeurAnaTMP36 = analogRead(A0) ; //on récupère la valeur lue par le microcontrôleur dans une variable 
    float tensionA0 = valeurAnaTMP36*5.0/1023 ; // on en déduit la tension appliquée sur A0
    temperature = (tensionA0-0.5)*100 ; //et on en déduit la température

	// acquisition de Réquivalente
    float valeurAnaUequiv = analogRead(A2) ;
	float Uequiv = valeurAnaUequiv*Ualim/1023.0 ; 
	float Requiv = R0*Uequiv/(Ualim-Uequiv) ;

    sommeTemperature = sommeTemperature + temperature ;
    sommeRequiv = sommeRequiv + Requiv ; 
    delay(200) ; 
    }

  //on prend le total et on moyenne sur les 20 tours de boucles
  temperature = sommeTemperature/20 ; 
  float Requiv = sommeRequiv/20 ; 


  // on affiche la température et la valeur de Réquiv.
  Serial.print(temperature);Serial.print(";");Serial.println(Requiv);

  delay(1000) ; 
  }
}
