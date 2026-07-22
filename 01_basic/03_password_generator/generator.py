import argparse
import string
import random

all_signs = string.printable
parser = argparse.ArgumentParser(
    prog='Pass-gen v3',
    description='Generate secure passwords using python script. Declare desired number of signs.'
)

def main():
    pass_length = int(input("Pass a number for your required password length: "))
    parser.add_argument('--use-symbols', action='store_true')
    parser.add_argument('--use-numbers', action='store_true')

    args = parser.parse_args()

main()