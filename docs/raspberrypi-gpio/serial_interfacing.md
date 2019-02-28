# Serial Interfacing

<!-- * Some general info on serial port -->
<!-- * LoRaWAN transmitter via COM -->

## Example

```python
import wiringpi
from time import sleep
import time

class LoRaWANForwarder(object):
  def __init__(self, serialdevice):
    wiringpi.wiringPiSetup()    # Use WiringPi numbering
    self.serial = wiringpi.serialOpen(serialdevice, 115200)  # Requires device/baud and returns an ID

  def read(self):
    while wiringpi.serialDataAvail(self.serial) > 0:
      value = (wiringpi.serialGetchar(self.serial))
      if value > 0:
        print("{}".format(chr(value)), end='', flush=True)

  def write(self, data):
    wiringpi.serialPutchar(self.serial, ord('['))   # Start of packet
    for c in data:
      print(c)
      wiringpi.serialPutchar(self.serial, ord(c))

    wiringpi.serialPutchar(self.serial, ord(']'))   # End of packet


## Main app
lora = LoRaWANForwarder('/dev/ttyACM0')

# Send message via serial every 10 seconds
start = end = time.time()
while True:
  # Print available data
  lora.read()
  sleep(0.1)
  end = time.time()
  if (end - start) > 10:
    start = end
    lora.write("12AA34")

```