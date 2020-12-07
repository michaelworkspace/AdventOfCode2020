#!/usr/bin/python3
import argparse
import subprocess

SESSION = '53616c7465645f5f38fa537c0a1f14af3b62ac25c9c60de95da5c5893e48f23f5415aa7c1f03ac86aad48dd33c7a0866'
parser = argparse.ArgumentParser(description='Read input')
parser.add_argument('day', type=int)
parser.add_argument('--year', type=int, default=2020)
args = parser.parse_args()

cmd = 'curl https://adventofcode.com/{}/day/{}/input --cookie "session={}"'.format(
        args.year, args.day, SESSION)
output = subprocess.check_output(cmd, shell=True)
print(output.decode('utf-8'), end='')
