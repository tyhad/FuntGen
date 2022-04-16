int i = 0, j = 0, k = 0, m = 0;
double t = 0, math = 0;
float amplitudo, frekuensi, fasa, d;
float phi = 3.14;
String data = "", data4[9];
char *data2 = NULL, data3[26];

void setup() {
  SerialUSB.begin(9600);
  analogWriteResolution(12);
  while (!SerialUSB) ;
  SerialUSB.println("MULAI");
  
  while (SerialUSB.available() == 0) {}
  data = SerialUSB.readString();
//  SerialUSB.println(data);
  
  data.toCharArray(data3, 26);
//  SerialUSB.println(data3);
    
  data2 = strtok(data3, ",");
  while(data2 != NULL)
  {
//    SerialUSB.println(data2);
    data4[m] = data2;
    SerialUSB.println(data4[m]);
    m = m+1;
    data2 = strtok(NULL, ",");
  }

}

void loop() {

  amplitudo = data4[0].toFloat();
  frekuensi = data4[1].toFloat();
  fasa      = data4[2].toFloat();
  SerialUSB.println(amplitudo);
  SerialUSB.println(frekuensi);
  SerialUSB.println(fasa);
  d = (2 * phi / frekuensi) + 0.01;
  j = d * 100;
  double myArray[j];

  for (t = 0; t <= d; t = t + 0.01) {
  math = amplitudo * sin(frekuensi * t + fasa);
//      SerialUSBUSB.println(math);
  myArray[i] = math;
  i = i + 1;
  }

  for (k = 0; k <= j; k++) {
  SerialUSB.println(myArray[k]);
  analogWrite(DAC0, myArray[k]);
  if (k == j){
    k = 0;
    }
  }
  
}
