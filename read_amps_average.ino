const int analogIn1 = A0, analogIn2 = A1, analogIn3 = A2, analogIn4 = A3, analogIn5 = A4, analogIn6 = A5;
int mVperAmp = 185;
int RawValue1, RawValue2, RawValue3, RawValue4, RawValue5, RawValue6 = 0;
int Offset4 = 2500, Offset5 = 2500, Offset6 = 2500;
double Voltage1, Voltage2, Voltage3, Voltage4, Voltage5, Voltage6 = 0;
double Amps1, Amps2, Amps3, Amps4, Amps5, Amps6 = 0;
double peakAmps1, peakAmps2, peakAmps3 = 0;
double avrPeakAmps1, avrPeakAmps2, avrPeakAmps3 = 0;
int startTime, endTime;
int avrStartTime, avrEndTime;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly;
  avrStartTime = millis();
  avrEndTime = avrStartTime;

  while ((avrEndTime - avrStartTime) <= 60000) {
    startTime = millis();
    endTime = startTime;
    while ((endTime - startTime) <= 100) {
      RawValue1 = analogRead(analogIn1);
      Voltage1 = (RawValue1 / 1023.0) * 5;
      Amps1 = (Voltage1 / 5.7) * 5;
      RawValue2 = analogRead(analogIn2);
      Voltage2 = (RawValue2 / 1023.0) * 5;
      Amps2 = (Voltage2 / 5.7) * 5;
      RawValue3 = analogRead(analogIn3);
      Voltage3 = (RawValue3 / 1023.0) * 5;
      Amps3 = (Voltage3 / 5.7) * 5;

      if (Amps1 > peakAmps1) {
        peakAmps1 = Amps1;
      }
      if (Amps2 > peakAmps2) {
        peakAmps2 = Amps2;
      }
      if (Amps3 > peakAmps3) {
        peakAmps3 = Amps3;
      }
      endTime = millis();
    }

    avrPeakAmps1 = (avrPeakAmps1 + peakAmps1) / 2;
    avrPeakAmps2 = (avrPeakAmps2 + peakAmps2) / 2;
    avrPeakAmps3 = (avrPeakAmps3 + peakAmps3) / 2;
    avrEndTime = millis();
    
    peakAmps1 = 0;
    peakAmps2 = 0;
    peakAmps3 = 0;
  }

  RawValue4 = analogRead(analogIn4);
  Voltage4 = (RawValue4 / 1023.0) * 5000;
  Amps4 = abs((Voltage4 - Offset4) / mVperAmp);

  RawValue5 = analogRead(analogIn5);
  Voltage5 = (RawValue5 / 1023.0) * 5000;
  Amps5 = abs((Voltage5 - Offset5) / mVperAmp);

  RawValue6 = analogRead(analogIn6);
  Voltage6 = (RawValue6 / 1023.0) * 5000;
  Amps6 = abs((Voltage6 - Offset6) / mVperAmp);

  //Serial.println (Amps1,3);
  //Serial.print (",");
  Serial.print (avrPeakAmps1, 3);
  Serial.print (",");
  Serial.print (avrPeakAmps2, 3);
  Serial.print (",");
  Serial.print (avrPeakAmps3, 3);
  Serial.print (",");
  Serial.print (Amps4, 3);
  Serial.print (",");
  Serial.print (Amps5, 3);
  Serial.print (",");
  Serial.println (Amps6, 3);
}
