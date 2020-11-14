#!/usr/bin/env python3

from psutil import virtual_memory

if __name__ == "__main__":
    print(' <span color="white">{}%</span>'.format(virtual_memory().percent))
