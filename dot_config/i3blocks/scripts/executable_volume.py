#!/usr/bin/env python3

import mouse
import nord
from subprocess import run, PIPE

volume_scroll_step = 1
icons = ('', '', '',)

if __name__ == "__main__":
    mouse_button = mouse.button()
    if mouse_button == mouse.BUTTON_LEFT:
        run(['pavucontrol', ])
    elif mouse_button == mouse.BUTTON_SCROLL_UP:
        run(['i3-volume', 'up', '{}'.format(volume_scroll_step)])
    elif mouse_button == mouse.BUTTON_SCROLL_DOWN:
        run(['i3-volume', 'down', '{}'.format(volume_scroll_step)])

    volume = run(['i3-volume', 'output', '%v'], check=False, stdout=PIPE).stdout.decode('utf-8')
    if volume == 'MUTE':
        print('婢')
    else:
        volume = float(volume[:-1])
        icon = icons[int((len(icons) * volume) / 100.0)]
        color = nord.AURORA[int((len(nord.AURORA) * volume) / 100.0)]
        print('{} <span color="{}">{}%</span>'.format(icon, color, volume))
