///**
//* Solar Panel Output Voltage Reading - arduino side
//* Pulau Geranting 
//*
//* @description
//* Algo: find peak voltage from 100 ms sample taken every 2 minutes
//* send to Raspberry Pi via Serial line
//* baud rate = 115200
//*
//* Author: Edward
//* Alva Energi
//* last edited: 18/2/2017
//**/

int readPinVolt = A0;
int readPinAmp = A3;
int voltValue = 0;
int ampValue = 0;

// sapling time loop variable
int startTime;
int endTime;
int peakVolt = 0;
int peakAmp = 0;

void setup() {
  pinMode(readPinVolt, INPUT);
  pinMode(readPinAmp, INPUT);
  Serial.begin(115200);
}

void loop() {
  startTime = millis();
  endTime = startTime;
 
  // read the voltage for 100 ms
  while((endTime - startTime) <= 100){
    voltValue = analogRead(readPinVolt);
    ampValue = analogRead(readPinAmp);
    
    // keep track of max value
    if (voltValue > peakVolt){
      peakVolt = voltValue;
    }
    
    // keep track of max value
    if (ampValue > peakAmp){
      peakAmp = ampValue;
    }
    
    endTime=millis();
  }

  // format file = Voltage, Ampere
  Serial.print(peakVolt);
  Serial.print(",");
  Serial.println(peakAmp);
  
  peakVolt = 0;
  peakAmp = 0;  

  // for debugging
  delay(1000);
  
  // pause for 5 minutes
  //delay(300000);
  
}

