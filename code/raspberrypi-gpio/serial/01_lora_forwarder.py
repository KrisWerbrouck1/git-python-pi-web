import wiringpi
from time import sleep
import time

wiringpi.wiringPiSetup()    # Use WiringPi numbering

serial = wiringpi.serialOpen('/dev/ttyACM0', 115200)  # Requires device/baud and returns an ID

# Send message via serial every 10 seconds
start = end = time.time()
while True:
  # Print available data
  while wiringpi.serialDataAvail(serial) > 0:
    value = (wiringpi.serialGetchar(serial))
    if value > 0:
      print("{}".format(chr(value)), end='', flush=True)
  sleep(0.1)
  end = time.time()
  if (end - start) > 10:
    start = end
    wiringpi.serialPuts(serial, "[10AA34]")

wiringpi.serialClose(serial)