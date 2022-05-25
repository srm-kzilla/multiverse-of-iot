import RPi.GPIO as gpio
import time
led = 15
gpio.setmode(gpio.BOARD)
gpio.setup(led, gpio.OUT)
while True:
  gpio.output(led, gpio.HIGH if input("Enter Y for switch on or any other key for off") == "Y" else gpio.LOW)
  time.sleep(1)
gpio.cleanup()
