double t=0;
double a=0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(t=0; t<=10; t=t+0.01){
    a = sin (1*t+5);
    Serial.print(t);
    Serial.print("   ");
    Serial.println(a);
  //  delay(10);
  }
}
