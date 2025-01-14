#!/usr/bin/env python3
"""
Author : cullyn <cullyn@localhost>
Date   : 2023-02-24
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    items = args.items
    num = len(items)

    if args.sorted:
        items.sort()

    if num == 1:
        print(f'You are bringing {items[0]}.')
    elif num == 2:
        print(f'You are bringing {items[0]} and {items[1]}.')
    else:
        items.insert(-1, 'and')
        itemlist = ', '.join(items[:-1])
        print(f'You are bringing {itemlist} {items[-1]}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
