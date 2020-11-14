#!/usr/bin/env python3

from psutil import sensors_temperatures
import sys

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print('300')
    else:
        temperature_list = sensors_temperatures()[sys.argv[1]]
        for temperature in temperature_list:
            if 'Package' in temperature.label:
                print(temperature.current)
                break
