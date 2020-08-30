import RPi.GPIO as GPIO
import time
import ultra_sonic as sonic
import buzzer

pin_buzzer = 16
pin_trig = 26
pin_echo = 20

def main():
    
    max_freq = 5000
    min_freq = 10
    max_dist = 266
    min_dist = 1
    try:
        while True:
            d = sonic.measure()
            #print(d)
            frequency = 10+(d/max_dist)*(max_freq-min_freq)
            #print(frequency)
            buzzer.bee(16, frequency*3, 0.01)  
            #time.sleep(0.1)
    except KeyboardInterrupt:
        GPIO.cleanup()


if __name__ == '__main__':
    main()