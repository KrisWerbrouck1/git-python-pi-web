import wiringpi
from time import sleep

wiringpi.wiringPiSetup()    # Use WiringPi numbering

touch = wiringpi.wiringPiI2CSetup(27)   # 0x1B

# Set internal pointer to register 3 (key state)
wiringpi.wiringPiI2CWrite(touch, 3)

# Start reading the key state
while True:
  sleep(0.1)
  value = wiringpi.wiringPiI2CRead(touch)
  print("State = {}".format(value))