import RPi.GPIO as GPIO
import time

pin_r = 19
pin_g = 13
pin_b = 6

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_r, GPIO.OUT)
GPIO.setup(pin_g, GPIO.OUT)
GPIO.setup(pin_b, GPIO.OUT)

GPIO.output(pin_r, GPIO.HIGH)
#GPIO.output(pin_g, GPIO.HIGH)
GPIO.output(pin_b, GPIO.HIGH)
time.sleep(5)
GPIO.output(pin_r, GPIO.LOW)
GPIO.output(pin_g, GPIO.LOW)
GPIO.output(pin_b, GPIO.LOW)

GPIO.cleanup()