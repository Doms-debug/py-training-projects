import socket

def check_single_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1.0)
    
    result = sock.connect_ex((target, port))
    
    if result == 0:
        print(f"Port {port} on host {target} is OPEN")
    else:
        print(f"Port {port} on host {target} is CLOSED")
        
    sock.close()

if __name__ == "__main__":
    check_single_port("1.1.1.1", 53)
    check_single_port("1.1.1.1", 9999)