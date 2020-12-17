#!/usr/bin/env python3

import nord
from subprocess import run, PIPE


def _get_package_data(commands, max_number):
    """
    Runs a list of commands, counts the packages returned by them and returns the number of packages and a colour.
    :param commands: Lists of commands (and their parameters) to execute.
    :param max_number: Above this number, the most intense colour will be used.
    :return: Tuple containing the colour and the number of packages
    """
    packages = []
    for command in commands:
        packages.extend(run(command, check=False, stdout=PIPE).stdout.decode('utf-8').split('\n'))
    number = sum(1 if len(package) > 0 else 0 for package in packages)
    colour_index = int((len(nord.AURORA) * min(1.0 * number, max_number - 1)) / (1.0 * max_number))
    return nord.AURORA[colour_index], number


if __name__ == "__main__":
    package_colour, package_number = _get_package_data([['checkupdates'], ['yay', '-Qua']], 25)
    orphan_colour, orphan_number = _get_package_data([['pacman', '-Qtdq'], ], 10)

    print(' <span color="{}">{}</span>  <span color="{}">{}</span>'.format(package_colour, package_number,
                                                                             orphan_colour, orphan_number))
