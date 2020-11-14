#!/usr/bin/env python3

from shutil import disk_usage

red_threshold = 90.0
yellow_threshold = 75.0

if __name__ == "__main__":
    disk_usage = disk_usage('/')
    disk_percent = round((100.0 * disk_usage.used) / disk_usage.total, 2)
    colour = 'white'
    if disk_percent > red_threshold:
        colour = 'red'
    elif disk_percent > yellow_threshold:
        colour = 'yellow'

    print(' <span color="{}">{}%</span>'.format(colour, disk_percent))
