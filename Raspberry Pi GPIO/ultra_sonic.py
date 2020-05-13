import RPi.GPIO as GPIO
import time

def measure(pin_t = 26, pin_e = 20):
    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_t, GPIO.OUT)
    GPIO.setup(pin_e, GPIO.IN)
    
    GPIO.output(pin_t, GPIO.HIGH)
    time.sleep(0.00015)
    GPIO.output(pin_t, GPIO.LOW)
    while not GPIO.input(pin_e):
        pass
    t1 = time.time()
    while GPIO.input(pin_e):
        pass
    t2 = time.time()
    return (t2-t1)*340*100/2

def main():
    try:
        while True:
            d = measure()
            print(d)
            time.sleep(0.3)
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    main()