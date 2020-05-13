import RPi.GPIO as GPIO

pin_led = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_led, GPIO.OUT)

pwm = GPIO.PWM(pin_led, 20) #frequency
pwm.start(50) # dc
input("按回车键继续")
pwm.stop()

GPIO.cleanup()