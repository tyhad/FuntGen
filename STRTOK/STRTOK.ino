char AnimalNames[] = "dog,cat,donkey,horse";
char *name = NULL;
void setup(){
  Serial.println(AnimalNames[0]);
    name = strtok(AnimalNames, ",");
    Serial.begin(9600);
    while(name != NULL)
    {
//        Serial.println(name);
        name = strtok(NULL, ","); 
    }
}
void loop() {
  // put your main code here, to run repeatedly:

}
