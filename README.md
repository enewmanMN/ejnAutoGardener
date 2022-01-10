# ejnAutoGardener
Automatic gardener with localhost monitoring

Would like to add display options for a variety of gardening statistics -- version 1 starting with soil moisture

To use the code you need to 
  upload the ino file to the arduino so that it can report its soil moisture readings thru the serial port
  start the python serialmonitor to read the moistureReadings and save them in a percentage format in soilReadings.csv file
  start the python gardenmonitor code to fire up a display on localhost for the readings
