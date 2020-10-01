from enum import Enum


class TimeDelay(Enum):
    MAX_DELAY = 1
    MIN_DELAY = 0.05
    DELAY_STEP = 0.05


def update_delay_time(delay_time, increment):
    delay_time += increment
    print(f"time delay, increment: {delay_time}, {increment}")
    delay_time = TimeDelay.MIN_DELAY.value if delay_time < TimeDelay.MIN_DELAY.value else delay_time
    delay_time = TimeDelay.MAX_DELAY.value if delay_time > TimeDelay.MAX_DELAY.value else delay_time
    return delay_time