#!/usr/bin/env python3
"""
Author : Ben Davis
Date   : 2021-05-05
Purpose: Emulate wc (word count)
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input file(s)',
                        default=[sys.stdin],
                        type=argparse.FileType('rt'),
                        nargs='*')

    parser.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Program entry point"""

    args = get_args()
    file = args.file

    total_lines = total_words = total_bytes = 0

    for fh in file:
        num_lines = num_words = num_bytes = 0

        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)

        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes

        print(f'{num_lines:8}{num_words:8}{num_bytes:8} {fh.name}')

    if len(file) > 1:
        print(f'{total_lines:8}{total_words:8}{total_bytes:8} total')


# --------------------------------------------------
if __name__ == '__main__':
    main()
