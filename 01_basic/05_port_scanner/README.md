```markdown
# Basic TCP port scanner

A commandline utility for scanning a range of TCP ports on a specified target IP address or domain. It identifies open ports and provides a summary of the scan results.

## Features

* Scans a continuous range of TCP ports
* Accepts IP addresses and domain names as targets
* Filters and displays only open ports
* Relies on standard Python libraries

## Setup and installation

* Navigate to the project directory
* No external dependencies or virtual environments are required

## Usage

Execute the script via terminal by providing the target address, the starting port number and the ending port number.

```bash
# Scan ports 50 to 100 on Cloudflare DNS server
python scanner.py 1.1.1.1 50 100

# Scan local development ports
python scanner.py 127.0.0.1 8000 8080

```

## Output

```text
$ python scanner.py 1.1.1.1 50 100
Scanning target 1.1.1.1 from port 50 to 100...

[+] Port 53 is OPEN
[+] Port 80 is OPEN

Scan completed. Found 2 open ports.

```

```

```