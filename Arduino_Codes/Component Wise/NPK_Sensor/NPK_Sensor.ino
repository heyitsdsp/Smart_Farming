# include "DHT.h"

# define NPIN 2
# define PPIN 3
# define KPIN 4
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

void setup() 
{
  Serial.begin(9600);
  N_SENSOR.begin();
  P_SENSOR.begin();
  K_SENSOR.begin();
}

void loop() 
{
  delay(2000);

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

  Serial.println("\n");
}
