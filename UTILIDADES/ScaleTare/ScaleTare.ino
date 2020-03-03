#include <SoftwareSerial.h>
#define RX    3   // *** D3, Pin 2
#define TX    4   // *** D4, Pin 3
SoftwareSerial Serial(RX, TX);

String str;
char c;

void setup(){
  pinMode(1, OUTPUT);
  Serial.begin(9600);  
}

void loop(){ 
  if(Serial.available() > 0){ 
    
    while(Serial.available() > 0){
      c = Serial.read();
      str += c;
      delay(10);
      }
      
    if(str == "Z"){
      digitalWrite(1, HIGH); // sets the digital pin 13 on
      delay(100);            // waits for a second
      digitalWrite(1, LOW);  // sets the digital pin 13 off
      }
    
    str = "";
  }
}
