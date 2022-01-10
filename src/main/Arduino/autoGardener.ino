int sensor_pin = A0; //signal from the capacitive soil moisture sensor
int output_value = 0;  // value of soil moisture
int pump = 3;      // digital pin where the relay is plugged in
int threshold = 50;  //threshold value to trigger pump (percent)
int lowestMoist = 572;
int highestMoist = 278;
int testAttempts = 0;
bool testRun = false;
int maxAttempts = 2;
const long thirtyMinutes = 1800000; // 30 minutes (1000ms x 60s x 30m)
const long fiveSeconds = 5000; // 5 seconds

void setup() {
  Serial.begin(9600);
//   Serial.println("_SOILFINAL_V1_");
  pinMode(sensor_pin, INPUT);  //setup for the soil moisture senor aka INPUt
  pinMode(pump, OUTPUT);      //setup for the pump aka   OUTPUT
//   Serial.println("Pump activation threshold %: ");
//   Serial.print(threshold);
}

void loop() {
    checkTestStatus();
    output_value = getSoilMoisturePercent();
    //Serial.print(output_value);
    if (output_value < threshold) {
        digitalWrite(pump, HIGH);
        //     Serial.println("pump on 5s");
        delay(fiveSeconds);  //run pump for 5 seconds;
        digitalWrite(pump, LOW);
        //Serial.println("pump off - delay 10s");
        //delay(300000); //wait 5 minutes
        //delay(10000); //wait 10 seconds before checking again  (switch to this line after testing)
    }
    else {
        digitalWrite(pump, LOW);
        //Serial.println("do not turn on pump - delay 20s");
        //delay(20000); //wait 20 seconds before checking again  (switch to this line after testing)
    }
    delay(thirtyMinutes); //wait 30 minutes before checking again
}

int getSoilMoisturePercent() {
    output_value = analogRead(sensor_pin);     //gets the value from the soil moisture sensor
//     Serial.print("Direct moisture reading:");
//     Serial.print(output_value);
    output_value = map(output_value,lowestMoist,highestMoist,0,100); // this sets the percentage value
//     Serial.print(" % Moisture Reading: ");
    Serial.print(output_value);
    return output_value;
}

void checkTestStatus() {
    if (testRun == true && testAttempts >= maxAttempts) {
        Serial.print("Test Over - threshold set: ");
        Serial.print(threshold);
        Serial.print(" Last moisture reading: ");
        Serial.print(output_value);
        Serial.print("End");
        exit(0);
    } else {
        testAttempts += 1;
//         Serial.print("Read attempt: ");
//         Serial.print(testAttempts);
//         Serial.print(" Max attempts: ");
//         Serial.print(maxAttempts);
    }
}

// TODO:  1.Need to change some variable names to make it more readable when we add monitoring variables
        //2.Remove some of the Serial.print calls and just make a logSer command or something.
        //3.Need to add some failsafes around the read commands to make sure we don't crash entirely
        //4.Will likely need to figure out a way to specify which reader we are adding to serial stream