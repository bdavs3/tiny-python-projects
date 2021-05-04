#!/usr/bin/env python3
"""
Author : Ben Davis
Date   : 2021-05-04
Purpose: Makes a statement about something spotted from the Crow's nest
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='A word')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Program entry point"""

    args = get_args()

    word = args.word
    article = 'an' if str.lower(word)[0] in 'aeiou' else 'a'

    print(f'Ahoy, Captain, {article} {word} off the larboard bow!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
