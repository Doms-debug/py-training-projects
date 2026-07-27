import argparse
import re
from collections import Counter
import sys

def main():
    parser = argparse.ArgumentParser(description="Extract and count IP addresses from a text file.")
    parser.add_argument("input_file", help="Path to the input log file")
    parser.add_argument("output_file", help="Path to the output results file")
    
    args = parser.parse_args()
    
    # regex pattern to match standard IPv4 addresses
    # \b ensures word boundaries so it doesn't match numbers inside longer strings
    ip_pattern = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b')
    
    try:
        with open(args.input_file, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{args.input_file}' was not found.")
        sys.exit(1)
        
    # find all strings matching the regex pattern
    extracted_ips = ip_pattern.findall(content)
    
    if not extracted_ips:
        print("No IP addresses found in the provided file.")
        sys.exit(0)
        
    # Counter automatically tallies occurrences and creates a dictionary-like object
    ip_counts = Counter(extracted_ips)
    
    try:
        with open(args.output_file, 'w', encoding='utf-8') as file:
            # most_common() returns a list of tuples sorted by frequency descending
            for ip, count in ip_counts.most_common():
                file.write(f"{ip} - {count}\n")
    except IOError as e:
        print(f"Error writing to file '{args.output_file}': {e}")
        sys.exit(1)
            
    print(f"Successfully extracted {len(extracted_ips)} total IPs.")
    print(f"Found {len(ip_counts)} unique IP addresses.")
    print(f"Results saved to '{args.output_file}'.")

if __name__ == '__main__':
    main()