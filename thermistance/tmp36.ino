// ce programme va permettre de lire la température sur le moniteur série

void setup(){
pinMode(A0, INPUT) ;//
Serial.begin(9600) ;//
}


void loop(){
float valeurAnaTMP36 = analogRead(A0) ;//
float tensionA0 =  ; //À COMPLÉTER
float temperature = ; //À COMPLÉTER

// on affiche la température
// À COMPLÉTER
delay(1000) ; //

}
