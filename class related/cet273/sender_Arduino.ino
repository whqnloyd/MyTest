#include<SPI.h>
#include<RF24.h>

RF24 radio(9, 10);    //set ce, csn pins
int msg[3];

void setup(){
  Serial.begin(9600);
  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x60);
  radio.openWritingPipe(0xF0F0F0F0A1LL);
  radio.enableDynamicPayloads();
  radio.powerUp();
}

void loop(){
  msg[0] = 1;
  msg[1] = 255;
  msg[2] = 255;
  radio.write(msg, sizeof(msg));
  Serial.println("sent message:");
  for(int i = 0; i < 3; i++){ Serial.println(i); }
  delay(1000);
  
  //const char text[] = "hello World";
  //radio.write(&text, sizeof(text));
  //delay(1000);
}
