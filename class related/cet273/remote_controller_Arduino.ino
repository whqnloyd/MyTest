#include <RF24.h>
#include <SPI.h>

RF24 radio(9,10);   //setup CE, CSN pins
int msg[3];   //setup your message 

int pin_x = A1;   //setup pins for joystick
int pin_y = A0;
int pin_b = 2;

int position_x = 0;   //setup your datas your want
int position_y = 0;
int state = 0;

void setup(){
  pinMode(pin_x, INPUT);
  pinMode(pin_y, INPUT);
  pinMode(pin_b, INPUT_PULLUP); 
  
  Serial.begin(9600); 
  radio.begin();
  radio.setPALevel(RF24_PA_MAX);
  radio.setChannel(0x60);
  radio.openWritingPipe(0xF0F0F0F0A1LL);
  radio.enableDynamicPayloads();
  radio.powerUp();
  }

void read_status(){
  position_x = analogRead(pin_x);
  position_y = analogRead(pin_y);

  if (digitalRead(pin_b) == 0){
    delay(300);
    if (digitalRead(pin_b) == 1){
      if (state == 0){ state = 1; }
      else { state = 0; }
      }
    }
  }

void customize(){
    
  }

void send_msg(){
  msg[0] = state;
  msg[1] = position_x;
  msg[2] = position_y;
  radio.write(msg, sizeof(msg));
  Serial.println("sent message:");
  for(int i = 0; i < 3; i++){ Serial.println(msg[i]); }
  delay(1000);
  }

void loop(){
  read_status();
  customize();
  send_msg();
  }
