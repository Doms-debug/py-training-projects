import argparse
import string
import random

all_letters = string.ascii_letters

parser = argparse.ArgumentParser(
    prog='Pass-gen v3',
    description='Generate secure passwords using python script. Declare desired number of signs.'
)

def main():
    parser.add_argument('length', type=int, help='Password length')
    parser.add_argument('--use-symbols', action='store_true')
    parser.add_argument('--use-numbers', action='store_true')

    args = parser.parse_args()

main()