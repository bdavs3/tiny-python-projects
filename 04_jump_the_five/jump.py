#!/usr/bin/env python3
"""
Author : Ben Davis
Date   : 2021-05-04
Purpose: Encrypt the numbers in a string
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Program entry point"""

    args = get_args()
    str_arg = args.str

    jumper = {
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5',
    }

    result = ''

    for char in str_arg:
        result += jumper.get(char, char)

    print(result)


# --------------------------------------------------
if __name__ == '__main__':
    main()
