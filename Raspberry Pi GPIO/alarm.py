import RPi.GPIO as GPIO
import time



def alarm():
    pin_r = 19
    pin_g = 13
    pin_b = 6
    pin_buzzer = 16

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_r, GPIO.OUT)
    GPIO.setup(pin_g, GPIO.OUT)
    GPIO.setup(pin_b, GPIO.OUT)
    GPIO.setup(pin_buzzer, GPIO.OUT)

    pwm_r = GPIO.PWM(pin_r, 10)
    pwm_g = GPIO.PWM(pin_g, 10)
    pwm_b = GPIO.PWM(pin_b, 10)
    pwm_buzzer = GPIO.PWM(pin_buzzer, 5)

    r = 50
    g = 0
    b = 0
    f = 50
    f_ = 0.5

    pwm_buzzer.start(50)

    try:
        while True:
            pwm_r.start(r)
            pwm_g.start(g)
            pwm_b.start(b)
            for x in range(400):
                if f>1 and f<101:
                    f+=f_
                else:
                    f_*=-1
                    f+=f_
                pwm_buzzer.ChangeFrequency(f*20)
                time.sleep(0.002)
            r,b=b,r
            b,g=g,b
            
    except KeyboardInterrupt:
        GPIO.cleanup()

if __name__ == '__main__':
    alarm()
