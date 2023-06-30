#!/usr/bin/env python3
"""
Author : cullyn <cullyn@localhost>
Date   : 2023-03-17
Purpose: Take text or file input and make it yell
"""

import argparse
import os
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper-cases input)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        metavar='str',
                        type=str,
                        help='Output filename')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """If text denotes a file, upper case contents, otherwise upper case text"""

    args = get_args()
    text = args.text
    outfile = args.outfile
    
    # Testing if this is a file, if so, read and upper case contents
    if os.path.isfile(text):
        fh = open(text)
        text = fh.read().rstrip().upper()
    else:
        text = text.upper()

    # If Outfile exists, write to a file, otherwise write to stdout
    if outfile:
        wfh = open(outfile, 'wt')
        wfh.write(text)
        wfh.close()
    else:
        print(text)

# --------------------------------------------------
if __name__ == '__main__':
    main()