#!/usr/bin/env python3

import nord
from subprocess import run, PIPE

max_num_packages = 25.0
""" Above this number, use the most intense colour. """

if __name__ == "__main__":
    packages = run(['checkupdates', ], check=False, stdout=PIPE).stdout.decode('utf-8').split('\n')
    num_packages = sum(1 if len(package) > 0 else 0 for package in packages)
    packages_aur = run(['yay', '-Qua'], check=False, stdout=PIPE).stdout.decode('utf-8').split('\n')
    num_packages += sum(1 if len(package) > 0 else 0 for package in packages_aur)
    index = int((len(nord.AURORA) * min(1.0 * num_packages, max_num_packages - 1)) / max_num_packages)
    colour = nord.AURORA[index]

    print(' <span color="{}">{}</span>'.format(colour, num_packages))
