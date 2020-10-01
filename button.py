from enum import Enum


class ButtonState(Enum):
    OFF = 0
    ON = 1
    UNDEFINED = 3


class PressedButtons(Enum):
    A = 0b10
    B = 0b01
    A_B = 0b11 
    NONE = 0


def get_button_state(codebug, button):
    if button != 'A' and button != 'B':
        return ButtonState.UNDEFINED
    if codebug.get_input(button) == 1:
        return ButtonState.ON
    else:
        return ButtonState.OFF


def button_handler(codebug):
    button_A = get_button_state(codebug, 'A').value
    button_B = get_button_state(codebug, 'B').value

    return PressedButtons(button_A << 1 | button_B)