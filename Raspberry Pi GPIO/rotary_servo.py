import RPi.GPIO as GPIO
import time as time

pin_rotary_push = 24
pin_rotary_left = 23
pin_rotary_right = 22

pin_servo = 12

def main():

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_rotary_left, GPIO.IN) # 电路板自带上拉电阻
    GPIO.setup(pin_rotary_push, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(pin_rotary_right, GPIO.IN) # 电路板自带上拉电阻
    GPIO.setup(pin_servo, GPIO.OUT)
    
    pwm = GPIO.PWM(pin_servo, 30) # 50->10  30->7
    pwm.start(0)
    
    angle = 90 # 自定义角度值, [0,180]取值区间
    maxdc = 7 # 占空比最大值, 要与频率综合考量， dc = maxdc*(angle/180)
    try:
        while True:
            if not GPIO.input(pin_rotary_push):
                angle = 90
                dc = maxdc*(angle/180)
                pwm.ChangeDutyCycle(dc)
                print("angle is: %i, dc is: %.2f"%(angle,dc))
                time.sleep(0.3)
            elif not GPIO.input(pin_rotary_left):
                if angle >0:
                    angle -= 1
                dc = maxdc*(angle/180)
                pwm.ChangeDutyCycle(dc)
                print("angle is: %i, dc is: %.2f"%(angle,dc))
                time.sleep(0.2)
            elif not GPIO.input(pin_rotary_right):
                if angle < 180:
                    angle += 1
                dc = maxdc*(angle/180)
                pwm.ChangeDutyCycle(dc)
                print("angle is: %i, dc is: %.2f"%(angle,dc))
                time.sleep(0.2)
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("Program is terminated, GPIO cleanup")
    
    
if __name__ == '__main__':
    main()
    exit(0)
