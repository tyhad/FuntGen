int i = 0, j = 0, k = 0;
double t = 0, math = 0;
float amplitudo, frekuensi, fasa;
float phi = 3.14, d;
String inString = "";

void setup() {
  SerialUSB.begin(9600);
  while (!SerialUSB) ;
  SerialUSB.println("Amplitudo");
}

void loop() {

  while (SerialUSB.available() == 0) {}
  //    inString = SerialUSB.readString();
  amplitudo = SerialUSB.parseFloat();
  SerialUSB.println(amplitudo);
  SerialUSB.println("Frekuensi");
  while (SerialUSB.available() == 0) {}
  //    inString = SerialUSB.readString();
  frekuensi = SerialUSB.parseFloat();
  SerialUSB.println(frekuensi);
  SerialUSB.println("Fasa");
  while (SerialUSB.available() == 0) {}
  //    inString = SerialUSB.readString();
  fasa = SerialUSB.parseFloat();
  SerialUSB.println(fasa);

  d = (2 * phi / frekuensi) + 0.01;
  j = d * 100;
  double myArray[j];
//    SerialUSB.println(d);
//    SerialUSB.println(j);
//    SerialUSB.println(sizeof(myArray));

  for (t = 0; t <= d; t = t + 0.01) {
    math = amplitudo * sin(frekuensi * t + fasa);
//        SerialUSB.println(math);
    myArray[i] = math;
    i = i + 1;
  }
  //  SerialUSB.println(i);
  //  SerialUSB.println(sizeof(myArray));

  for (k = 0; k <= j; k++) {
    SerialUSB.println(myArray[k]);
    //    delay(9);
  }
}
