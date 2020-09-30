
//CODE FOR Analog pH Sensor (Just get the value and print)

# include "DHT.h"

# define PHPIN 2
# define PHTYPE DHT22

DHT dht(PHPIN, PHTYPE);

float read_pH()
{
  return dht.readHumidity();
}

void setup() 
{
  Serial.begin(9600);     //Baud rate = 9600
  dht.begin();            //Start up the sensor              
}

void loop() 
{
  delay(2000);            //Essential delay because pH sensor needs some time to stabilize

  float pH_value = read_pH();

  if(isnan(pH_value))
  {
    Serial.println("Failed to read from sensor");
    return;
  }

  Serial.print("pH: ");
  Serial.println(pH_value);
}
