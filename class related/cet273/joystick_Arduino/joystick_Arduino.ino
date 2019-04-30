int pin_x = A1;
int pin_y = A0;
int pin_b = 2;

int position_x = 0;
int position_y = 0;
int b_now = 0;
int num = 0;

void setup(){
  // initialize serial communications at 9600 bps
  Serial.begin(9600); 
  // set pin mod as INPUT
  pinMode(pin_x, INPUT);
  pinMode(pin_y, INPUT);
  //activate pull-up resistor on the push-button pin, then the voltage will be stable.
  pinMode(pin_b, INPUT_PULLUP); 
  }

void button(){
  b_now = digitalRead(pin_b);
  if (b_now == 0){
    delay(300);
    b_now = digitalRead(pin_b);
    if (b_now == 1){
      if (num == 0){
        num = 1;
        }
      else {
        num = 0;
        }
      }
    }
  }

void read_show(){
  position_x = analogRead(pin_x);
  position_y = analogRead(pin_y);

  button();

  Serial.print("X: ");
  Serial.print(position_x);
  Serial.print(" | Y: ");
  Serial.print(position_y);
  Serial.print(" | Button: ");
  Serial.println(num);

  delay(100); // add some delay between reads
  }

void loop(){
  read_show();
  }
