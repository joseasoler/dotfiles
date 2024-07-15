#!/usr/bin/env python3

import argparse
import mouse
import nord
import psutil
from shutil import disk_usage
from subprocess import run, PIPE

_default_temperature = (0.0, 50.0, 70.0)
""" Temperatures used when a sensor cannot be found or when one of its values are invalid. """

_separator = '<span color="grey"> | </span>'

_temp_labels = ('', '', '', '', '')
""" Labels used for regular, (between regular and high), high, (between high and critical) and critical temps. """

_power_label = ''
""" Label used for power draw values. """

_usage_suffix = '%'
""" Suffix for usage values measured in percentages. """

_temp_suffix = '°C'
""" Suffix for temperatures measured in Celsius. """

_power_suffix = 'W'
""" Suffix for power draw values measured in Watts. """

_usage_high = 80.0
""" Usage high threshold. """

_usage_critical = 96.0
""" Usage critical threshold. """

_cpu_usage_label = '󰘚'
""" Label for CPU usage. """

_gpu_usage_label = '󰾲'
""" Label for GPU usage. """

_ram_usage_label = '󰍛'
""" Label for RAM usage. """

_disk_usage_label = ' '
""" Label for disk usage. """


def _round(value):
    """ round redefinition for using the same format consistently. """
    return round(value, 1)


def _to_pango(label, threshold_list, suffix):
    """
    Formats a value in pango.
    :param label: String with the label, or a list containing the label for regular, high and critical.
    :param threshold_list: List containing the current value, the high threshold and the critical threshold.
    :param suffix: Suffix to add after the value.
    :return: string containing the value formatted in pango.
    """
    index = 0
    if threshold_list[0] > threshold_list[2]:
        index = 4
    elif threshold_list[0] > ((threshold_list[2] + threshold_list[1]) / 2.0):
        index = 3
    elif threshold_list[0] > threshold_list[1]:
        index = 2
    elif threshold_list[0] > (threshold_list[1] / 2.0):
        index = 1

    lbl = label if isinstance(label, str) else label[index]
    return '{} <span color="{}">{}{}</span>'.format(lbl, nord.AURORA[index], _round(threshold_list[0]), suffix)


def _to_average_temp(name, temperature_map):
    """
    Converts the list of temperatures associated to a label to a list of average temperatures.
    If the sensor does not exist, it will return _default_temperature. If the high or critical temperature thresholds
    are invalid, it will use the values from _default_temperature instead.
    :param name: Name of the sensor to check.
    :param temperature_map: Dictionary of temperatures, as returned by psutil.sensors_temperatures
    :return: List containing the current, high and critical temperatures of the label.
    """
    if name not in temperature_map:
        return _default_temperature

    temps = [0.0, 0.0, 0.0]
    for temp in temperature_map[name]:
        current = temp.current if temp.current is not None and temp.current > -50.0 else _default_temperature[0]
        high = temp.high if temp.high is not None and temp.high > 0.0 else _default_temperature[1]
        critical = temp.critical if temp.critical is not None and temp.critical > 0.0 else _default_temperature[2]
        temps[0] += current
        temps[1] += high
        temps[2] += critical

    size = float(len(temperature_map[name]))
    temps[0] = _round(temps[0] / size)
    temps[1] = _round(temps[1] / size)
    temps[2] = _round(temps[2] / size)

    return temps


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--cpu", type=str, required=True, help="CPU sensor label")
    parser.add_argument("-r", "--ram", type=str, required=True, help="RAM sensor label")
    parser.add_argument("-d", "--disk", type=str, required=True, nargs='+',
                        help="List of paths to a mounted disk and, optionally, @ and then a sensor label")
    args = parser.parse_args()

    if mouse.button() == mouse.BUTTON_LEFT:
        run(['kitty', 'btop'])
    elif mouse.button() == mouse.BUTTON_RIGHT:
        run(['gwe', ])

    temperatures = psutil.sensors_temperatures()

    # CPU data
    cpu_usage = float(psutil.cpu_percent(interval=1.0, percpu=False))
    output = _to_pango(_cpu_usage_label, (cpu_usage, _usage_high, _usage_critical), _usage_suffix)
    # ToDo Review with the data of the Zen 3 temperature sensor when the 5.10 kernel is released.
    output = output + ' ' + _to_pango(_temp_labels, _to_average_temp(args.cpu, temperatures), _temp_suffix)

    # GPU data
    gpu_data = run(('nvidia-smi', '--query-gpu=utilization.gpu,temperature.gpu,power.draw,power.limit',
                    '--format=csv,noheader,nounits'), check=False, stdout=PIPE).stdout.decode('utf-8')
    gpu_usage, gpu_temp, gpu_power, gpu_power_limit = [float(value) for value in gpu_data.replace('\n', '').split(', ')]

    output = output + _separator + _to_pango(_gpu_usage_label, (gpu_usage, _usage_high, _usage_critical), _usage_suffix)
    output = output + ' ' + _to_pango(_temp_labels, (gpu_temp, 70, 80), _temp_suffix)
    output = output + ' ' + _to_pango(_power_label, (gpu_power, gpu_power_limit * 0.9, gpu_power_limit), _power_suffix)

    # RAM data
    ram_usage = float(psutil.virtual_memory().percent)
    output = output + _separator + _to_pango(_ram_usage_label, (ram_usage, _usage_high, _usage_critical), _usage_suffix)
    output = output + ' ' + _to_pango(_temp_labels, _to_average_temp(args.ram, temperatures), _temp_suffix)

    # Disk data
    for d in args.disk:
        d_data = d.split('@')
        d_usage = disk_usage(d_data[0])
        d_percent = _round((100.0 * d_usage.used) / d_usage.total)
        output = output + _separator + _to_pango(_disk_usage_label, (d_percent, _usage_high, _usage_critical),
                                                 _usage_suffix)
        if len(d_data) > 1:
            output = output + ' ' + _to_pango(_temp_labels, _to_average_temp(d_data[1], temperatures), _temp_suffix)

    print(output)
