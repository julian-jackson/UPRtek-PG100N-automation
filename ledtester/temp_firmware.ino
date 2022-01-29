// the number of the LED pin

// setting PWM properties
const int freq = 5000;
const int resolution = 8;
const int trialspacing = 3500;
const int totaltrials = 4;

void setup(){
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
  // configure LED PWM functionalitites
  ledcSetup(0, freq, resolution);
  ledcSetup(1, freq, resolution);
  ledcSetup(2, freq, resolution);
  ledcSetup(3, freq, resolution);
  ledcSetup(4, freq, resolution);
  
  // attach the channel to the GPIO to be controlled
  ledcAttachPin(32, 0); // WHITE
  ledcAttachPin(33, 1); // RED
  ledcAttachPin(26, 2); // GREEN
  ledcAttachPin(25, 3); // BLUE
  ledcAttachPin(27, 4); // FAR RED
  
}
 
//void loop(){
  // increase the LED brightness
//  for(int dutyCycle = 0; dutyCycle <= 255; dutyCycle++){   
//    // changing the LED brightness with PWM
//    ledcWrite(ledChannel, dutyCycle);
//    delay(15);
//  }
  
//  delay(100000);
//}
void loop() {
  if (Serial.available()) { // if there is data comming
    String command = Serial.readStringUntil('\n'); // read string until newline character

    if (command == "test") {
      for(int i = 1; i <= totaltrials; i++){
        for(int j = 0; j <= 4; j++){
      
          ledcWrite(j, (255 / totaltrials) * (i));
          Serial.println((255 / totaltrials) * (i));
          delay(trialspacing);
          ledcWrite(j, 0);
        }
      }
    } else if (command == "ping") {
      digitalWrite(LED_BUILTIN, HIGH);  // turn off LED
      Serial.println("pong");
    } else if (command.substring(0, 1) == "w") {
      ledcWrite(0, command.substring(1).toInt());
    } else if (command.substring(0, 1) == "r") {
      ledcWrite(1, command.substring(1).toInt());
    } else if (command.substring(0, 1) == "g") {
      ledcWrite(2, command.substring(1).toInt());
    } else if (command.substring(0, 1) == "b") {
      ledcWrite(3, command.substring(1).toInt());
    } else if (command.substring(0, 1) == "f") {
      ledcWrite(4, command.substring(1).toInt());
    } else if (command == "cll") {
      ledcWrite(0, 0);
      ledcWrite(1, 0);
      ledcWrite(2, 0);
      ledcWrite(3, 0);
      ledcWrite(4, 0);
    } 
  }
}
