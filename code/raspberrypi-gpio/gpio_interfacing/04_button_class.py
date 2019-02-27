import wiringpi
from time import sleep

class Button(object):
  def __init__(self, pin):
    self.pinNumber = pin
    wiringpi.wiringPiSetup()    # Use WiringPi numbering
    wiringpi.pinMode(self.pinNumber, 0)        # Set button pin to 0 ( INPUT )

  def get_state(self):
    return wiringpi.digitalRead(self.pinNumber)

# The main program
button = Button(25)

while True:
  print("The push button state = {}".format(button.get_state()))
  sleep(1)