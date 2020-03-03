String str;
float weight = 0.0;
char c;

void setup(){
  Serial.begin(9600);  
}

void loop(){ 
  if(Serial.available() > 0){ 
    
    while(Serial.available() > 0){
      c = Serial.read();
      str += c;
      delay(10);
      }
      
    if(str == "R"){
      if(weight == 0.0){
        Serial.println("\x02     0.00 kg GR");
        weight = 10.0;
        delay(10);
        }
      else{
        Serial.println("\x02    " + String(weight) + " kg GR");
        weight += 5.5;
        delay(10);
      }
    }

    if(str == "Z"){
      weight = 0.0;
      delay(10);
      }
    
    str = "";
 }
}
