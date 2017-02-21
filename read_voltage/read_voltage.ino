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

int readPin = A0;
int sensorValue = 0;

// sapling time loop variable
int startTime;
int endTime;
int peakVolt = 0;

void setup() {
  pinMode(readPin, INPUT);
  Serial.begin(115200);
}

void loop() {
  startTime = millis();
  endTime = startTime;
 
  // read the voltage for 100 ms
  while((endTime - startTime) <= 100){
    sensorValue = analogRead(readPin);
    //Serial.println(sensorValue);
    
    // keep track of max value
    if (sensorValue > peakVolt){
      peakVolt = sensorValue;
    }
    
    endTime=millis();
  }

  Serial.println(peakVolt);
  peakVolt = 0;  

//  // for debugging
  delay(5000);
  
  // pause for 5 minutes
  //delay(300000);
  
}

