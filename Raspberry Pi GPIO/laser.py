import RPi.GPIO as GPIO
import time

def irradiate(pin_laser, frequency, duration):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_laser, GPIO.OUT)
    pwm = GPIO.PWM(pin_laser, frequency)
    pwm.start(50)
    time.sleep(duration)
    pwm.stop()

def main():
    try:
        while True:
            irradiate(5, 10, 1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        
if __name__ == '__main__':
    main()