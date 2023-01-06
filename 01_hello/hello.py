#!/Users/cullyn/miniconda3/envs/tinypy/bin/python
# Purpose: To say hello.

import argparse

parser = argparse.ArgumentParser(description='Say hello!')
parser.add_argument('-n', '--name', metavar='name', default='World', help='Name to greet')
args = parser.parse_args()
print('Hello, ' + args.name + '!')