#!/usr/bin/env python3

import mouse
from os import path
from processor import ProcessorData, processor_status
from subprocess import run

core = 'coretemp'

util_data = ProcessorData(args=('python', '-c', 'import psutil; print(psutil.cpu_percent(interval=0.5, percpu=False))'),
                          thresholds=((' <span color="red">{}%</span>', 85.0),
                                      (' <span color="yellow">{}%</span>', 60.0),
                                      (' <span color="white">{}%</span>',)))

temp_data = ProcessorData(args=('{}/cpu_temperature.py'.format(path.dirname(__file__)), core,),
                          thresholds=((' <span color="red">{}°C</span>', 90.0),
                                      (' <span color="yellow">{}°C</span>', 70.0),
                                      (' <span color="white">{}°C</span>',)))

if __name__ == "__main__":
    if mouse.button() == mouse.BUTTON_LEFT:
        run(['alacritty', '-e', 'bpytop', '-s'])
    print(processor_status(util_data, temp_data))
