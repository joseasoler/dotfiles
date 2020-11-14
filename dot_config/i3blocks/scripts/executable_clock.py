#!/usr/bin/env python3

from datetime import datetime
import mouse
from subprocess import Popen

if __name__ == "__main__":
    mouse_button = mouse.button()
    if mouse_button == mouse.BUTTON_LEFT:
        Popen(['gsimplecal', ])

    date_time = datetime.now()
    date = date_time.strftime('%d/%m')
    time = date_time.strftime('%H:%M:%S')
    print(' <span color="white">{}</span>  <span color="white">{}</span>'.format(date, time))
