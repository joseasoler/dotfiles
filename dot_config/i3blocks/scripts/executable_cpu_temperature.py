#!/usr/bin/env python3

from psutil import sensors_temperatures
import sys

if __name__ == "__main__":
    temperature_map = sensors_temperatures()
    if len(sys.argv) <= 1 or sys.argv[1] not in temperature_map:
        print('300')
    else:
        # ToDo Improve with the data of the Zen 3 temperature sensor when the 5.10 kernel is released.
        print(temperature_map[sys.argv[1]][0].current)
