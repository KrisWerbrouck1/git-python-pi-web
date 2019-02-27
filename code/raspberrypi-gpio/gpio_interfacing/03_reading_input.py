import wiringpi
from time import sleep

wiringpi.wiringPiSetup()    # Use WiringPi numbering

PIN_NUMBER = 25

wiringpi.pinMode(PIN_NUMBER, 0)        # Set Pushbutton pin to 0 ( INPUT )

while True:
  state = wiringpi.digitalRead(PIN_NUMBER)
  print("The push button state = {}".format(state))
  sleep(1)