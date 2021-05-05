#!/usr/bin/env python3
"""
Author : Ben Davis
Date   : 2021-05-05
Purpose: Uppercase some text
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Uppercase some text',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Program entry point"""

    args = get_args()
    text = args.text
    outfile = args.outfile

    if os.path.isfile(text):
        fh = open(text)
        text = fh.read()

    text = text.upper()

    if outfile != '':
        fh = open(outfile, 'wt')
        fh.write(text)
        fh.close()
    else:
        print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
