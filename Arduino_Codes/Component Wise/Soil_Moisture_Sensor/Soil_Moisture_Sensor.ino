# define sensor_pin A0

void setup() 
{
  Serial.begin(9600);
  pinMode(sensor_pin, INPUT);
}

void loop() 
{
  delay(2000);
  float output_value = analogRead(sensor_pin);

  Serial.print("Soil mositure: ");
  Serial.println(output_value);
}
