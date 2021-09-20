'''
Author: your name
Date: 2021-08-28 19:34:45
'''
import time
from enum import Enum, auto

from HCSR501_driver import HCSR501Driver
from servo_driver import ServoDriver
from config import (STOP_TIME, INTERVER_TIME)


class State(Enum):
    idle = auto()
    scare = auto()
    intermediate = auto()


def main():
    servo_driver = ServoDriver()
    HCSR501_driver = HCSR501Driver()

    state = State.idle
    time_count = 0
    while True:
        if HCSR501_driver.detect():
            if state == State.idle:
                servo_driver.start()
            state = State.scare
            time_count = 0
        elif time_count == STOP_TIME:
            servo_driver.stop()
            state = State.idle
            time_count = 0
        else:
            state = State.intermediate
            time_count += INTERVER_TIME
        time.sleep(INTERVER_TIME)


if __name__ == '__main__':
    main()
