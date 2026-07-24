import argparse
import string
import random

all_letters = string.ascii_letters

parser = argparse.ArgumentParser(
    prog='Pass-gen v3',
    description='''
    Generate secure passwords using python script. 
    Declare desired number of signs.
    '''
)

def main():
    parser.add_argument('length', type=int, help='Password length')
    parser.add_argument('--use-symbols', action='store_true', help='Include punctuation marks')
    parser.add_argument('--use-numbers', action='store_true', help='Include digits')

    args = parser.parse_args()

    # start with the base pool of letters
    character_pool = all_letters

    # dynamically expand the pool based on user flags
    if args.use_numbers:
        character_pool += string.digits
        
    if args.use_symbols:
        character_pool += string.punctuation

    # random.choices picks 'k' elements from the pool (allows duplicates)
    generated_chars = random.choices(character_pool, k=args.length)

    # join the list elements into one string
    final_password = "".join(generated_chars)

    print(final_password)

if __name__ == '__main__':
    main()