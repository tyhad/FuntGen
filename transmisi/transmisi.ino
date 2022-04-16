int i;
String math;
String ini [10] = {};

void setup() {
  Serial.begin(9600);

}

void loop() {
  Serial.println("start");
  while (Serial.available() == 0) {}
  math = Serial.readString();

  for(i=0; i<=11; i++){
      Serial.println(math.substring(i));
//    ini [i] = math;
//    Serial.println(ini [i]);
  }
}
