#define kpa2atm 0.00986923267
// pin defs
int pressurePin = 0;

// variables
int val;
float pkPa; // pressure in kPa
float pAtm; // pressure in Atm
double soil_moisture;

unsigned long time;
# include "DHT.h"

#define DHTPIN 6
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);
# define NPIN 5
# define PPIN 4
# define KPIN 3
# define TYPE DHT22

DHT N_SENSOR(NPIN, TYPE);
DHT P_SENSOR(PPIN, TYPE);
DHT K_SENSOR(KPIN, TYPE);

float read_n()
{
  return N_SENSOR.readHumidity();
}

float read_p()
{
  return P_SENSOR.readHumidity();
}

float read_k()
{
  return K_SENSOR.readHumidity();
}
# define PHPIN 7
# define PHTYPE DHT22

DHT ph(PHPIN, PHTYPE);

float read_pH()
{
  return ph.readHumidity();
}
# define sensor_pin A1

void setup() {
   Serial.begin(9600);
   dht.begin();
   N_SENSOR.begin();
  P_SENSOR.begin();
  K_SENSOR.begin();
  pinMode(sensor_pin, INPUT);
  pinMode(A5, OUTPUT);

}

void loop() {
  val = analogRead(pressurePin);
  pkPa = ((float)val/(float)1023+0.095)/0.009;
  pAtm = kpa2atm*pkPa;
  
 
  /* send pressure to serial port */
  Serial.print(pkPa);
  Serial.print("kPa ");
  Serial.print(pAtm);
  Serial.println("Atm ");


  
  delay(200);           //Essential delay between measurements because DHT22 is a finicky sensor


  float Relative_Humidity = dht.readHumidity();             //Read the humidity from the sensor 
  float Absolute_Temperature = dht.readTemperature();       //Read the temperature from the sensor in degree celsius
  float output_value;

  if(isnan(Relative_Humidity) || isnan(Absolute_Temperature))     //This check is necessary because sometimes the DHT gives NaN errors
  {
    Serial.println("Failed to read from sensor!");
    return;
  }

  Serial.print("Humidity: ");
  Serial.println(Relative_Humidity);

  Serial.print("\tTemperature: ");
  Serial.println(Absolute_Temperature);

  delay(200);

  float n_value = read_n();
  float p_value = read_p();
  float k_value = read_k();

  if(isnan(n_value) || isnan(p_value) || isnan(k_value))
  {
    Serial.println("Failed to read from a sensor!");
    return;
  }

  Serial.print("N_VALUE: ");
  Serial.println(n_value);

  Serial.print("P_VALUE: ");
  Serial.println(p_value);

  Serial.print("K_VALUE: ");
  Serial.println(k_value);

  //Serial.println("\n");



   delay(200);            //Essential delay because pH sensor needs some time to stabilize

  float pH_value = read_pH();

  if(isnan(pH_value))
  {
    Serial.println("Failed to read from sensor");
    return;
  }

  Serial.print("pH: ");
  Serial.println(pH_value);


   delay(200);
  output_value = analogRead(sensor_pin);
  output_value = 100-((output_value/1023)*100);
  soil_moisture = output_value;

  Serial.print("Soil mositure: ");
  Serial.print(soil_moisture);
  Serial.println(" %");

  if(soil_moisture <= 40)
  {
    digitalWrite(A5, HIGH);
  }
  else
  {
    digitalWrite(A5, LOW);
  }

  delay(2000);

  Serial.println("\n");  
}
