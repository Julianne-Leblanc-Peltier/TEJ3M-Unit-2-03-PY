# Created by: Julianne Leblanc-Peltier
# Created on: April 2025
#
#  Turns an LED on for one second, then off for one second, repeatedly.

import time
import board
import digitalio

led = digitalio.DigitalInOut(board.GP5)
led.direction = digitalio.Direction.OUTPUT

blink_time = 1

# loop forever
while True:
    print(blink_time)
    led.value = True # turns LED on
    time.sleep(blink_time) # wait for 1000ms
    led.value = False # turns LED off
    time.sleep(blink_time) # wait for 1000ms
