import wiringpi
from time import sleep

class Led(object):
  def __init__(self, pin):
    self.pinNumber = pin
    wiringpi.wiringPiSetup()    # Use WiringPi numbering
    wiringpi.pinMode(self.pinNumber, 1) # As output
    self.off()

  def on(self):
    self.set_state(True)

  def off(self):
    self.set_state(False)

  def toggle(self):
    self.set_state(not self.get_state())

  def set_state(self, state):
    self.isOn = state
    wiringpi.digitalWrite(self.pinNumber, state)   # Write state to LED pin

  def get_state(self):
    return self.isOn

# The main program
led = Led(4)

while True:
  print("Toggling the LED")
  led.toggle()
  sleep(1)