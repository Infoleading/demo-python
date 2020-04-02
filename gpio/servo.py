import RPi.GPIO as GPIO
import time

pin_servo = 12

def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_servo, GPIO.OUT)
    
    pwm = GPIO.PWM(pin_servo, 50)
    pwm.start(0)
    
    try:
        while True:
            for dc in range(0, 110, 5):
                pwm.ChangeDutyCycle(dc/10)
                time.sleep(0.05)             
            for dc in range(110, 0, -5):
                pwm.ChangeDutyCycle(dc/10)
                time.sleep(0.05)        
    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    main()
    exit(0)