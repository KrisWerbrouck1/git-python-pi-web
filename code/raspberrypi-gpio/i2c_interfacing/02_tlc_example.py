import wiringpi
from time import sleep

wiringpi.wiringPiSetup()    # Use WiringPi numbering

leds = wiringpi.wiringPiI2CSetup(0x60)   # 0x60

# Setup the device for PWM
for i in range(0,3):
  wiringpi.wiringPiI2CWriteReg8(leds, 0x14+i, 0xAA)
  sleep(0.1)

# Enable oscillator
wiringpi.wiringPiI2CWriteReg8(leds, 0x00, 0x00)
sleep(0.1)

# Set a led
FIRST_LED = 0x02
wiringpi.wiringPiI2CWriteReg8(leds, FIRST_LED+3, 0x45)