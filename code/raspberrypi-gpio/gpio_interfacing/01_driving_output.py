import wiringpi
from time import sleep

wiringpi.wiringPiSetup()    # Use WiringPi numbering

PIN_NUMBER = 4

wiringpi.pinMode(PIN_NUMBER, 1)        # Set LED pin to 1 ( OUTPUT )

while True:
  print("Setting LED on")
  wiringpi.digitalWrite(PIN_NUMBER, 0)   # Write 0 ( LOW ) to LED pin
  sleep(1)
  print("Setting LED off")
  wiringpi.digitalWrite(PIN_NUMBER, 1)   # Write 1 ( HIGH ) to LED pin
  sleep(1)