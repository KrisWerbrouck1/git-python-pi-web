from time import sleep
import sys
from touchberrypi import TouchberryPi
from touchberrypi import Color
from touchberrypi import Colors
from touchberrypi import Led
from touchberrypi import TouchKey

shield = TouchberryPi()

colors = [Colors.RED, Colors.GREEN, Colors.CYAN, Colors.MAGENTA]

interval = 0.3
currentLed = 0
colorIndex = 0
delta = 1
partyMode = False

def on_key_down(key):
    global interval
    global colorIndex
    global partyMode

    if key == TouchKey.UP:
        interval = interval / 2.0
    elif key == TouchKey.DOWN:
        interval = interval * 2.0
    elif key == TouchKey.X:
        colorIndex = (colorIndex + 1) % len(colors)
    elif key == TouchKey.B:
        partyMode = not partyMode

shield.on_key_down(on_key_down)
shield.set_all_leds(Colors.BLACK)
shield.start_touch_listener(0.1)

while True:
    shield.set_all_leds(Colors.BLACK)
    shield.set_led(currentLed,colors[colorIndex])
    currentLed = (currentLed + delta)

    if currentLed >= 4 or currentLed <= 0:
        delta = -delta
        if partyMode:
            colorIndex = (colorIndex + 1) % len(colors)

    sleep(interval)