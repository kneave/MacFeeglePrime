#include "SerialTransfer.h"
SerialTransfer myTransfer;

#define hwserial Serial1

// the setup routine runs once when you press reset:
void setup() {
  
  pinMode(2, INPUT_PULLDOWN);
  pinMode(3, INPUT_PULLDOWN);
  pinMode(4, INPUT_PULLDOWN);
  pinMode(5, INPUT_PULLDOWN);
  pinMode(6, INPUT_PULLDOWN);
  pinMode(7, INPUT_PULLDOWN);
  pinMode(8, INPUT_PULLDOWN);
  pinMode(9, INPUT_PULLDOWN);
  
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
  
  hwserial.begin(115200);
//  myTransfer.begin(hwserial);
}

// the loop routine runs over and over again forever:
void loop() {
  int sensorValueLX = (analogRead(A0) - 512) * -1;
  int sensorValueLY = (analogRead(A1) - 512) * -1;
  int sensorValueLZ = analogRead(A2) - 512;

  int sensorValueRX = (analogRead(A3) - 512) * -1;
  int sensorValueRY = (analogRead(A4) - 512) * -1;
  int sensorValueRZ = analogRead(A5) - 512;
  int sensorValuePot = analogRead(A6);
  
  int buttonPressL = digitalRead(2);
  int buttonPressR = digitalRead(3);

  int switch1 = digitalRead(4);
  int switch2 = digitalRead(5);

  //  3 and 4 are the three way switch
  int switch3 = digitalRead(6);
  int switch4 = digitalRead(7);
  
  int switch5 = digitalRead(8);
  int switch6 = digitalRead(9);

  // print out the value you read:
  String rightStick = String(sensorValueRX) + "," + 
                      String(sensorValueRY) + "," + 
                      String(sensorValueRZ) + "," + 
                      String(buttonPressR);

  String leftStick = String(sensorValueLX) + "," + 
                     String(sensorValueLY) + "," + 
                     String(sensorValueLZ) + "," + 
                     String(buttonPressL);
                     
  int threeway = switch3 - switch4;

  String buttons =  String(switch1) + "," +
                    String(switch2) + "," +
                    String(threeway) + "," +
                    String(switch5) + "," +
                    String(switch6) + "," +
                    String(sensorValuePot);
                    
  Serial.println(leftStick + "," + rightStick + "," + buttons);
  hwserial.println(leftStick + "," + rightStick + "," + buttons);
  
  //  Prep and send bytes to Pi
//  myTransfer.txBuff[0] = sensorValueLX;
//  myTransfer.txBuff[1] = sensorValueLY;
//  myTransfer.txBuff[2] = sensorValueLZ;
//  myTransfer.txBuff[3] = buttonPressL;
//  
//  myTransfer.txBuff[4] = sensorValueRX;
//  myTransfer.txBuff[5] = sensorValueRY;
//  myTransfer.txBuff[6] = sensorValueRZ;
//  myTransfer.txBuff[7] = buttonPressR;
//  
//  myTransfer.txBuff[8] = switch1;
//  myTransfer.txBuff[9] = switch2;
//  myTransfer.txBuff[10] = threeway;
//  myTransfer.txBuff[11] = switch5;
//  myTransfer.txBuff[12] = switch6;
//  myTransfer.txBuff[13] = sensorValuePot;

//  myTransfer.sendData(14);
    
  delay(20);        // delay in between reads for stability
}
