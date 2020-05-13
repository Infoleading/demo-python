import RPi.GPIO as GPIO
import time

pin_led = 21
pin_button = 17

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_led, GPIO.OUT)
GPIO.setup(pin_button, GPIO.IN, GPIO.PUD_UP)

s = 0
while True:
    if not GPIO.input(pin_button):
        if s == 0:
            s = 1
        else:
            s = 0
        time.sleep(0.5)
        
    if s==1:
        GPIO.output(pin_led, GPIO.HIGH)
    else:
        GPIO.output(pin_led, GPIO.LOW)
    
GPIO.cleanup()

