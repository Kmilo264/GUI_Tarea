
long randomNumber;

void setup() {
  
  Serial.begin(9600);
  randomSeed(analogRead(A0));  
      
}
 
void loop() {
  
  randomNumber = random(1,20);
  
  //Escribimos el numero aleatorio por el puerto serie
  Serial.println(randomNumber);
  delay(1000);
}
