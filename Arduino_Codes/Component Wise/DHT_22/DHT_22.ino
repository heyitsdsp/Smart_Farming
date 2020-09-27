
//CODE FOR DHT22 Sensor (Just get the values and print)
 
# include "DHT.h"

#define DHTPIN 2
#define DHTTYPE DHT22

DHT dht(DHTPIN, DHTTYPE);

void setup()
{
  Serial.begin(9600);     //Baud rate = 9600
  dht.begin();            //Start up the sensor          
}

void loop()
{
  delay(2000);            //Essential delay between measurements because DHT22 is a finicky sensor

  float Relative_Humidity = dht.readHumidity();             //Read the humidity from the sensor 
  float Absolute_Temperature = dht.readTemperature();       //Read the temperature from the sensor in degree celsius

  if(isnan(Relative_Humidity) || isnan(Absolute_Temperature))     //This check is necessary because sometimes the DHT gives NaN errors
  {
    Serial.println("Failed to read from sensor!");
    return;
  }

  Serial.print("Humidity: ");
  Serial.print(Relative_Humidity);

  Serial.print("\tTemperature: ");
  Serial.println(Absolute_Temperature);
}
