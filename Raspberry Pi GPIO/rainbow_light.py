import RPi.GPIO as GPIO
import time



if __name__ == '__main__':
    pin_r = 19
    pin_g = 13
    pin_b = 6
    pin_buzzer = 16

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin_r, GPIO.OUT)
    GPIO.setup(pin_g, GPIO.OUT)
    GPIO.setup(pin_b, GPIO.OUT)
    GPIO.setup(pin_buzzer, GPIO.OUT)

    pwm_r = GPIO.PWM(pin_r, 100)
    pwm_g = GPIO.PWM(pin_g, 100)
    pwm_b = GPIO.PWM(pin_b, 100)
    pwm_buzzer = GPIO.PWM(pin_buzzer, 5)

    r = 1
    r_ = r
    g = 2
    g_ = g
    b = 4
    b_ = b
    f = 50
    f_ = 1
    pwm_r.start(0)
    pwm_g.start(0)
    pwm_b.start(0)
    pwm_buzzer.start(50)

    try:
        while True:
            if r>0 and r<100:
                r+=r_
            elif g>0 and g<100:
                r_*=-1
                r+=r_
                g+=g_
            elif b>0 and b<100:
                r_*=-1
                g_*=-1
                r+=r_
                g+=g_
                b+=b_
            else:
                r_*=-1
                g_*=-1
                b_*=-1
                r+=r_
                g+=g_
                b+=b_
                
            if f>1 and f<101:
                f+=f_
            else:
                f_*=-1
                f+=f_
                
            pwm_r.ChangeDutyCycle(r)
            pwm_g.ChangeDutyCycle(g)
            pwm_b.ChangeDutyCycle(b)
            pwm_buzzer.ChangeFrequency(f*20)
            #print(r)
            #print(g)
            #print(b)
            #print(f)
            time.sleep(0.05)
    except KeyboardInterrupt:
        GPIO.cleanup()

