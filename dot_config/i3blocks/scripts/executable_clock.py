#!/usr/bin/env python3

from datetime import datetime
import mouse
import nord
from subprocess import Popen

if __name__ == "__main__":
    mouse_button = mouse.button()
    if mouse_button == mouse.BUTTON_LEFT:
        Popen(['firefox', '-new-tab', 'https://calendar.google.com', ])

    date_time = datetime.now()
    date = date_time.strftime('%d/%m')
    time = date_time.strftime('%H:%M:%S')
    print(' <span color="{}">{}</span>   <span color="{}">{}</span>'.
          format(nord.SNOW[2], date, nord.SNOW[2], time))
