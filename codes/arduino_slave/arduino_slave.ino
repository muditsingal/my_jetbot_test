int motor1pin1 = 2;
int motor1pin2 = 3;
int motor1pwm = 9;

int motor2pin1 = 4;
int motor2pin2 = 5;
int motor2pwm = 10;

void setup() {
  Serial.begin(115200);
//  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(motor1pin1, OUTPUT);
  pinMode(motor1pin2, OUTPUT);
  pinMode(motor2pin1, OUTPUT);
  pinMode(motor2pin2, OUTPUT);
  pinMode(motor1pwm, OUTPUT); 
  pinMode(motor2pwm, OUTPUT);
}

String rx_data;
String cmd;
int left_wh_speed;
int right_wh_speed;

void loop() {
  if(Serial.available())
  {
    cmd = Serial.read();
    left_wh_speed = Serial.read();
    right_wh_speed = Serial.read();
    left_wh_speed = left_wh_speed -127;
    right_wh_speed = right_wh_speed -127;
//    if(left_wh_speed == 121)
//    {
//      digitalWrite(LED_BUILTIN, HIGH);
//      delay(500);  
//    }
//    digitalWrite(LED_BUILTIN, LOW);
//    delay(500); 
//    
  }
  
  if(left_wh_speed < 0)
  {
    digitalWrite(motor1pin1, LOW);
    digitalWrite(motor1pin2, HIGH);
    analogWrite(motor1pwm,left_wh_speed*2);
  }
  else
  {
    digitalWrite(motor1pin1, HIGH);
    digitalWrite(motor1pin2, LOW);
    analogWrite(motor1pwm,left_wh_speed*2);
  }


  if(right_wh_speed < 0)
  {
    digitalWrite(motor2pin1, LOW);
    digitalWrite(motor2pin2, HIGH);
    analogWrite(motor2pwm,right_wh_speed*2);
  }
  else
  {
    digitalWrite(motor2pin1, HIGH);
    digitalWrite(motor2pin2, LOW);
    analogWrite(motor2pwm,right_wh_speed*2);
  }
  
}
