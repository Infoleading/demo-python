import RPi.GPIO as GPIO
import time

pin_buzzer = 16

def bee(pin_b, frequency, duration):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_b, GPIO.OUT)
    pwm = GPIO.PWM(pin_b, frequency)
    pwm.start(50)
    time.sleep(duration)
    pwm.stop()

def main():
    try:
        while True:
            bee(pin_buzzer, 50, 3)
    except KeyboardInterrupt:
        GPIO.cleanup()
    
if __name__ == '__main__':
    main()