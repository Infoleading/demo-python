import RPi.GPIO as GPIO
import time as time

pin_rotary_push = 24
pin_rotary_left = 23
pin_rotary_right = 22



def main():
    num = 0
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_rotary_left, GPIO.IN) # 电路板自带上拉电阻
    GPIO.setup(pin_rotary_push, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(pin_rotary_right, GPIO.IN) # 电路板自带上拉电阻
    
    try:
        while True:
            if not GPIO.input(pin_rotary_push):
                num = 0
                print("number:%i"%num)
                time.sleep(0.3)
            elif not GPIO.input(pin_rotary_left):
                num = num-1
                print("number:%i"%num)
                time.sleep(0.1)
            elif not GPIO.input(pin_rotary_right):
                num = num+1
                print("number:%i"%num)
                time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Program is terminated, GPIO cleanup")
    
    
if __name__ == '__main__':
    main()
    exit(0)