const int analogIn1 = A0, analogIn2 = A1, analogIn3 = A2, analogIn4 = A3, analogIn5 = A4, analogIn6 = A5;
int mVperAmp = 185;
int RawValue1, RawValue2, RawValue3, RawValue4, RawValue5, RawValue6 = 0;
int Offset1 = 2505, Offset2 = 2495, Offset=3 = 2500, Offset4 = 2500, Offset5 = 2500, Offset6 = 2500;
double Voltage1, Voltage2, Voltage3, Voltage4, Voltage5, Voltage6 = 0;
double Amps1, Amps2, Amps3, Amps4, Amps5, Amps6 = 0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  RawValue1 = analogRead(analogIn1);
  Voltage1 = (RawValue1/1024.0)*5000;
  Amps1 = (Voltage1 - Offset1)/mVperAmp;

  RawValue2 = analogRead(analogIn2);
  Voltage2 = (RawValue2/1024.0)*5000;
  Amps2 = (Voltage2 - Offset2)/mVperAmp;

  RawValue3 = analogRead(analogIn3);
  Voltage3 = (RawValue3/1024.0)*5000;
  Amps3 = (Voltage3 - Offset3)/mVperAmp;

  RawValue4 = analogRead(analogIn4);
  Voltage4 = (RawValue4/1024.0)*5000;
  Amps4 = (Voltage4 - Offset4)/mVperAmp;

  RawValue5 = analogRead(analogIn5);
  Voltage5 = (RawValue5/1024.0)*5000;
  Amps5 = (Voltage5 - Offset5)/mVperAmp;

  RawValue6 = analogRead(analogIn6);
  Voltage6 = (RawValue6/1024.0)*5000;
  Amps6 = (Voltage6 - Offset6)/mVperAmp;
  
  Serial.println (Amps1,3);
  Serial.print (",");
  Serial.println (Amps2,3);
  Serial.print (",");
  Serial.println (Amps3,3);
  Serial.print (",");
  Serial.println (Amps4,3);
  Serial.print (",");
  Serial.println (Amps5,3);
  Serial.print (",");
  Serial.println (Amps6,3);
  
  delay(30000);  
}
