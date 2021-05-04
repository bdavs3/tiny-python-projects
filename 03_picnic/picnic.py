#!/usr/bin/env python3
"""
Author : Ben Davis
Date   : 2021-05-04
Purpose: Picnic game
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bring some items to a picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        action='store_true',
                        help='Sort the items (default: False)')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Program entry point"""

    args = get_args()
    items = args.items
    sort = args.sorted

    if sort:
        list.sort(items)

    if len(items) == 1:
        str_items = f'{items[0]}'
    elif len(items) == 2:
        str_items = f'{items[0]} and {items[1]}'
    else:
        items[-1] = f'and {items[-1]}'
        str_items = ', '.join(items)

    print(f'You are bringing {str_items}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
