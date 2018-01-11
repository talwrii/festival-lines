# make code as python 3 compatible as possible
from __future__ import absolute_import, division, print_function, unicode_literals

import argparse
import re
import sys
import festival

def build_parser():
    PARSER = argparse.ArgumentParser(description='Say lines as they arrive')
    PARSER.add_argument('--period', default=1.0, type=float, help='Have festival talk faster or slower')
    PARSER.add_argument('--speed', default=1.0, dest='period', type=invfloat, help='Have festival talk faster or slower')
    PARSER.add_argument('regex', nargs='*', help='Only say things matching these regular expressions')
    args = PARSER.parse_args()
    return PARSER

def main():
    args = build_parser().parse_args()
    festival.setStretchFactor(args.period)
    while True:
        line = sys.stdin.readline()
        if line == '':
            break
        print(line, end='')
        if (not args.regex) or any(re.search(r, line) for r in args.regex):
            festival.sayText(line.decode('utf8').encode('ascii', errors='replace'))

def invfloat(string):
    return 1. / float(string)


