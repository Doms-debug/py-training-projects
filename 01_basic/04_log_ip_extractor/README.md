# Log IP Extractor

A command-line utility designed to parse raw text files, such as web server logs, and extract IPv4 addresses. The tool automatically counts the frequency of each unique IP and exports a sorted summary to a specified output file.

## Features

* Uses regular expressions to accurately identify IPv4 addresses within raw text
* Automatically counts and sorts IPs by their frequency of occurrence
* Exports clean, formatted results to a new text file
* Includes basic error handling for missing files and input/output operations

## Setup and Installation

* Navigate to the project directory
* No external dependencies or virtual environments are required as the script uses only built-in Python modules

## Usage

Execute the script via terminal by providing the path to the input log file and the desired output file name.

```bash
# Extract IPs from sample.log and save the results to output.txt
python extractor.py sample.log output.txt