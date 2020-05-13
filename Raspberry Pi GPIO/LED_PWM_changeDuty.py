import RPi.GPIO as GPIO
import time

pin_led = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_led, GPIO.OUT)

pwm = GPIO.PWM(pin_led, 50)
pwm.start(0)

try:
    while 1: 
        for dc in range(0, 101, 5):
            pwm.ChangeDutyCycle(dc)
            #print("dc1=%i"%dc)
            time.sleep(0.1)
        for dc in range(100, 1, -5):
            pwm.ChangeDutyCycle(dc)
            #print("dc2=%i"%dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    print("Stop pwm OK!")

pwm.stop()

GPIO.cleanup()
            