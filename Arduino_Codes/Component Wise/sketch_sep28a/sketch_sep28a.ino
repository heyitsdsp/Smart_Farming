#define kpa2atm 0.00986923267


// pin defs
int pressurePin = 0;

// variables
int val;
float pkPa; // pressure in kPa
float pAtm; // pressure in Atm

unsigned long time;


void setup()
{
  Serial.begin(9600);
 
}

void loop()
{
  
  /* get the pressure */
  val = analogRead(pressurePin);
  pkPa = ((float)val/(float)1023+0.095)/0.009;
  pAtm = kpa2atm*pkPa;
  
 
  /* send pressure to serial port */
  Serial.print(pkPa);
  Serial.print("kPa ");
  Serial.print(pAtm);
  Serial.println("Atm ");
  delay(1000);
}
