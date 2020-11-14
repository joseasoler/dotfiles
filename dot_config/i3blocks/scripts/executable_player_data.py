#!/usr/bin/env python3

from subprocess import run, PIPE

player_status = {'Playing': '', 'Paused': '', 'Stopped': ''}

if __name__ == "__main__":
    status = run(['playerctl', 'status'], check=False, stdout=PIPE).stdout.decode('utf-8').split('\n')[0]
    if status not in player_status:
        print('')
    else:
        metadata = run(['playerctl', 'metadata', '--format', '{{ title }}'], check=False, stdout=PIPE).stdout.decode(
            'utf-8').split('\n')[0]
        print('{} {}'.format(player_status[status], metadata))
