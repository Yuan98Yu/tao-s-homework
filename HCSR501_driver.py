'''
Author: YY
Date: 2021-08-28 19:31:38
References: https://zhuanlan.zhihu.com/p/76143231
'''
import RPi.GPIO as GPIO


def HCSR501Driver(object):
    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(8, GPIO.IN)
        GPIO.setup(40, GPIO.OUT)
        GPIO.setup(3, GPIO.OUT)

    def detect(self) -> bool:
        return GPIO.input(8)
