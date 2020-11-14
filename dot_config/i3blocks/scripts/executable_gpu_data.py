#!/usr/bin/env python3

import mouse
from processor import ProcessorData, processor_status
from subprocess import run

util_data = ProcessorData(args=('nvidia-smi', '--query-gpu=utilization.gpu', '--format=csv,noheader,nounits'),
                          thresholds=((' <span color="red">{}%</span>', 99.0),
                                      (' <span color="yellow">{}%</span>', 70.0),
                                      (' <span color="white">{}%</span>',)))

temp_data = ProcessorData(args=('nvidia-smi', '--query-gpu=temperature.gpu', '--format=csv,noheader,nounits'),
                          thresholds=((' <span color="red">{}°C</span>', 85.0),
                                      (' <span color="yellow">{}°C</span>', 75.0),
                                      (' <span color="white">{}°C</span>',)))

if __name__ == "__main__":
    if mouse.button() == mouse.BUTTON_LEFT:
        run(['nvidia-settings', ])
    print(processor_status(util_data, temp_data))
