import RPi.GPIO as gpio
import time
led = 15
switch = 5
gpio.setmode(gpio.BOARD)
gpio.setup(switch, gpio.IN, pull_up_down=gpio.PUD_UP)
gpio.setup(led, gpio.OUT)
while True:
  gpio.output(led, gpio.input(switch))
  time.sleep(1)
gpio.cleanup()
