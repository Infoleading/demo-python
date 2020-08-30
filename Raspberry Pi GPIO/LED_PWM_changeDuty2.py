import RPi.GPIO as GPIO
import time
import math

pin_led = 19

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_led, GPIO.OUT)

pwm = GPIO.PWM(pin_led, 100)
pwm.start(0)
a = 0
try:
    while 1:
        dc = 50+math.sin(a)*50
        pwm.ChangeDutyCycle(dc)
        print("dc=%i"%dc)
        time.sleep(0.05)
        a+=0.05
except KeyboardInterrupt:
    print("Stop pwm OK!")

pwm.stop()

GPIO.cleanup()
            