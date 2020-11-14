#!/usr/bin/env python3

from subprocess import run, PIPE

if __name__ == "__main__":
    packages = run(['checkupdates', ], check=False, stdout=PIPE).stdout.decode('utf-8').split('\n')
    num_packages = sum(1 if len(package) > 0 else 0 for package in packages)
    colour = 'white' if num_packages == 0 else 'yellow'

    print(' <span color="{}">{}</span>'.format(colour, num_packages))
