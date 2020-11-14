import os

BUTTON_NONE = -1
BUTTON_LEFT = 1
BUTTON_MIDDLE = 2
BUTTON_RIGHT = 3
BUTTON_SCROLL_UP = 4
BUTTON_SCROLL_DOWN = 5


def button():
    return int(os.getenv('button', BUTTON_NONE))
