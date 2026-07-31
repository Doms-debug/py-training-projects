import argparse
import socket
import sys

def is_port_open(target, port):
    """
    Attempts to connect to a specific port on the target.
    Returns True if the port is open, False otherwise.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Reduced timeout to speed up scanning over large ranges
    sock.settimeout(0.5)
    
    result = sock.connect_ex((target, port))
    sock.close()
    
    return result == 0

def main():
    parser = argparse.ArgumentParser(description="Basic TCP port scanner")
    parser.add_argument("target", help="Target IP address or domain (like 127.0.0.1 or google.com)")
    parser.add_argument("start_port", type=int, help="Starting port number")
    parser.add_argument("end_port", type=int, help="Ending port number")
    
    args = parser.parse_args()
    
    # Basic validation to ensure port numbers are within valid ranges
    if args.start_port < 1 or args.end_port > 65535 or args.start_port > args.end_port:
        print("Error: Invalid port range provided.")
        sys.exit(1)
        
    print(f"Scanning target {args.target} from port {args.start_port} to {args.end_port} \n")
    
    open_ports_found = 0
    
    # The range() function stops before the second argument, so we add 1
    for port in range(args.start_port, args.end_port + 1):
        if is_port_open(args.target, port):
            print(f"[+] Port {port} is OPEN")
            open_ports_found += 1
            
    print(f"\nScan completed. Found {open_ports_found} open ports.")

if __name__ == "__main__":
    main()