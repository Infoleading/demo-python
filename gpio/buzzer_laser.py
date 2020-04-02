import RPi.GPIO as GPIO
import time
import buzzer
import laser

def main():
    try:
        while True:
            frequency = 10
            duration = 3
            buzzer.bee(16, frquency, duration)
            