import RPi.GPIO as GPIO
import time

pin_led = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_led, GPIO.OUT)
#GPIO.output(pin_led, GPIO.LOW)

a = 0.01
try:
    while True:
        GPIO.output(pin_led, GPIO.HIGH)
        time.sleep(a/2)
        GPIO.output(pin_led, GPIO.LOW)
        time.sleep(a)
except KeyboardInterrupt:
    GPIO.cleanup()
