import codebug_tether
import time
from time_delay import TimeDelay, update_delay_time
from button import PressedButtons, button_handler

# SLEEP_TIME_MIN = 0.1
# SLEEP_TIME_MAX = 1
# SLEEP_TIME_STEP = 0.1
# SLEEP_TIME = 0.5


codebug = codebug_tether.CodeBug()


def set_main_diagonal():
    codebug.clear()
    codebug.set_pixel(0, 0, 1)
    codebug.set_pixel(1, 1, 1)
    codebug.set_pixel(2, 2, 1)
    codebug.set_pixel(3, 3, 1)
    codebug.set_pixel(4, 4, 1)


def set_reverse_diagonal():
    codebug.clear()
    codebug.set_pixel(0, 4, 1)
    codebug.set_pixel(1, 3, 1)
    codebug.set_pixel(2, 2, 1)
    codebug.set_pixel(3, 1, 1)
    codebug.set_pixel(4, 0, 1)


def set_vertical():
    codebug.clear()
    codebug.set_col(2, 0b11111)


def set_horizontal():
    codebug.clear()
    codebug.set_row(2, 0b11111)


def get_delay_time(delay_time, pressed_buttons):
    if pressed_buttons == PressedButtons.A:
        return update_delay_time(delay_time, -TimeDelay.DELAY_STEP.value)
    if pressed_buttons == PressedButtons.B:
        return update_delay_time(delay_time, TimeDelay.DELAY_STEP.value)
    return delay_time


def main():
    sleep_time = TimeDelay.MIN_DELAY.value
    try:
        while True:
            set_vertical()
            time.sleep(sleep_time)
            set_main_diagonal()
            time.sleep(sleep_time)
            set_horizontal()
            time.sleep(sleep_time)
            set_reverse_diagonal()
            time.sleep(sleep_time)
            pressed_buttons = button_handler(codebug)
            sleep_time = get_delay_time(sleep_time, pressed_buttons)
            # print(sleep_time)

    except KeyboardInterrupt:
        pass



if __name__ == "__main__":
    main()