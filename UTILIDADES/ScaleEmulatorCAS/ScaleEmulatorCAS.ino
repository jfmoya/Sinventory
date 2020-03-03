String in_ms;
String out_ms;
String pre = "ST,GS,";
String pos = " kg";
float weight = 0.0;
String weight_s;
char c;
byte len;
byte d_len; 

void setup(){
  Serial.begin(9600);  
}

void loop(){ 
  if(Serial.available() > 0){ 
    
    while(Serial.available() > 0){
      c = Serial.read();
      in_ms += c;
      delay(10);
      }
      
    if(in_ms == "\x00"){
      if(weight == 0.0){
        Serial.print(pre);
        Serial.write(0x00);
        Serial.print("\xc4,");
        Serial.print("     0.0");
        Serial.println(pos);
        weight = random(150, 500);
        weight = weight / 10;
        delay(10);
        }
      else{
        weight_s = String(weight);
        
        len = weight_s.length();
        weight_s.remove(len-1);
        d_len = 8 + 1 - len; // +1: por que el nuevo len es menos 1
        //Serial.println(d_len);
        delay(10);
        for (int i = 0; i < d_len; i++) {
          weight_s = " "+weight_s;
        }
        out_ms = weight_s+pos;
        Serial.print(pre);
        Serial.write(0x00);
        Serial.write("\xc4,");
        Serial.println(out_ms);
        weight += 5.5;
        delay(10);
      }
    }

    if(in_ms == "Z"){
      weight = 0.0;
      delay(10);
      }
    
    in_ms = "";
 }
}
