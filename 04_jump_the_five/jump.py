#!/usr/bin/env python3
"""
Author : cullyn <cullyn@localhost>
Date   : 2023-03-10
Purpose: Learning Dictionaries
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the Five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='str',
                        help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    input = args.input

    jumper = {'1':'9','2':'8','3':'7','4':'6','5':'0','6':'4','7':'3','8':'2','9':'1','0':'5'}

    for char in input:
        if char in jumper:
            char = jumper.get(char)
            print(char,end='')
        else:
            print(char,end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
