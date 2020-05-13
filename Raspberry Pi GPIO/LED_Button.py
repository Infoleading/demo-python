import RPi.GPIO as GPIO
import time

pin_led = 21
pin_button = 17

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_led, GPIO.OUT)
GPIO.setup(pin_button, GPIO.IN, GPIO.PUD_UP)

while True:
    if not GPIO.input(pin_button):
        GPIO.output(pin_led, GPIO.HIGH)
    else:
        GPIO.output(pin_led, GPIO.LOW)
    
GPIO.cleanup()

