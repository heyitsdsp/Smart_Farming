#define soil_moisture A1    //soil moisture sensor data pin
#define pressure A0         //pressure sensor data pin
#define kpa2atm 0.00986923267   //conversion factor bet'n kpa to atm
#include "DHT.h"      //include DHT library
#define DHTPIN 6        // DHT sensor data pin
#define DHTTYPE DHT11   //include DHT type
#define PHPIN 2        //PH sensor data pin
#define NPIN A2        //Nitrogen data pin
#define PPIN A3        //Phosporous data pin
#define KPIN A4        //Potassium data pin
#define Valvepin A5     //valve data pin
// variables defining
int val;    // variables defining
float pkPa; // pressure in kPa
float pAtm; // pressure in Atm

DHT dht(DHTPIN, DHTTYPE); //define DHT function

void setup() 
{
  Serial.begin(9600);            //send data at port 9600
  dht.begin();                   //start DHT
  pinMode(soil_moisture, INPUT); //start soil moisture sensor
  pinMode(PHPIN, INPUT);         //start pH sensor
  pinMode(NPIN, INPUT);          //start N sensor
  pinMode(PPIN, INPUT);          //start P sensor
  pinMode(KPIN, INPUT);          //start K sensor
  pinMode(Valvepin, OUTPUT);     //valve pin
}

void loop() 
{
  delay(1500);                                //getting soil moisture
  Serial.println("Reading Data");
  delay(1000);
  float moisture = analogRead(soil_moisture);       //getting soil moisture
  moisture = (moisture/1023)*100;       //getting soil moisture

  if(isnan(moisture))                           //Adding failsafe for NaN values
  {
    Serial.println("Failed to read from soil misture sensor!");
    return;
  }
  
  else{
  Serial.print("Soil mositure: ");            //printing soil moisture
  Serial.print(moisture);                   //printing soil moisture
  Serial.println(" %");}                //printing soil moisture
  
  delay(1000);
  val = analogRead(pressure);                  //getting pressure
  pkPa = ((float)val/(float)1023+0.095)/0.009; //getting pressure
  pAtm = kpa2atm*pkPa;                         //getting pressure

  if(isnan(pressure))     //Adding failsafe for NaN values
  {
    Serial.println("Failed to read from pressure sensor!");
    return;
  }

  else{
  Serial.print("Pressure in kPa: ");                         //printing pressure
  Serial.println(pkPa);                         //printing pressure
  Serial.print("Pressure in Atm: ");                         //printing pressure
  Serial.println(pAtm);}                  //printing pressure
  
  delay(1000);           
  float Relative_Humidity = dht.readHumidity();       //Read the humidity 
  float Absolute_Temperature = dht.readTemperature(); //Read the temperature

  if(isnan(Relative_Humidity) || isnan(Absolute_Temperature))     //Adding failsafe for NaN values
  {
    Serial.println("Failed to read from DHT sensor!");
    return;
  }
  else{
  Serial.print("Humidity: ");           //print H and T
  Serial.println(Relative_Humidity*10);      //print H and T
  Serial.print("\tTemperature: ");      //print H and T
  Serial.println(Absolute_Temperature*10);} //print H and T

  delay(1000);            
  float pH_value = analogRead(PHPIN); //read pH value

  if(isnan(pH_value))    //Adding failsafe for NaN values
  {
    Serial.println("Failed to read from pH sensor!");
    return;
  }

  else{
  Serial.print("pH level is: ");     //print pH value
  Serial.println(pH_value/71.43);}  //print pH value

  delay(1000);
  float n_value = analogRead(NPIN);  //getting N value  
  float p_value = analogRead(PPIN);  //getting P value
  float k_value = analogRead(KPIN);  //getting K value

  if(isnan(n_value) || isnan(p_value) || isnan(k_value))     //Adding failsafe for NaN values
  {
    Serial.println("Failed to read from NPK sensor!");
    return;
  }

  else{
  delay(300);
  Serial.print("N VALUE (ppm): ");    //printing N value
  Serial.println(n_value/28.57);      //printing N value

  delay(300);
  Serial.print("P VALUE (ppm): ");    //printing P value
  Serial.println(p_value/40);      //printing P value

  delay(300);
  Serial.print("K VALUE (ppm): ");    //printing K value
  Serial.println(k_value/20); }     //printing K value

  if(moisture <= 40)            //condition for motor to start
  {
    digitalWrite(Valvepin, HIGH);     //condition for motor to start
    Serial.println("Valve open");
  }
  else
  {
    digitalWrite(Valvepin, LOW);      //condition for motor to stop
    Serial.println("Valve closed");
  }

  delay(1000);
  Serial.println("\n");  
}
