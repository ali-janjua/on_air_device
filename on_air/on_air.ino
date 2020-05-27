/* 
  "On Air" Lamp for Microsoft Teams
*/

#define button_mute 2

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(button_mute, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(button_mute), mute_unmute, RISING);
  digitalWrite(LED_BUILTIN, LOW);
  Serial.begin(9600);
}

void mute_unmute() {
  static unsigned long last_interrupt_time = 0;
  detachInterrupt(digitalPinToInterrupt(button_mute));
  unsigned long interrupt_time = millis();

  // If interrupts come faster than 200ms, assume it's a bounce and ignore
  if (interrupt_time - last_interrupt_time > 200)
  {
    Serial.print(HIGH);
  }

  last_interrupt_time = interrupt_time;
  attachInterrupt(digitalPinToInterrupt(button_mute), mute_unmute, RISING);
}

void loop() {
  if (Serial.available() > 0) {
    
    char comdata = Serial.read();

    if (comdata == '1' ) {
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if (comdata == '0' ) {
      digitalWrite(LED_BUILTIN, LOW);
    } 
  }
  
}
