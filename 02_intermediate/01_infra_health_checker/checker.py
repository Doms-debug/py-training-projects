import psutil

def get_cpu_usage():
    """Returns the current system-wide CPU utilization as a percentage."""
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    """Returns the current RAM utilization as a percentage."""
    mem = psutil.virtual_memory()
    return mem.percent

def get_disk_usage(path="/"):
    """Returns the disk utilization for the specified path as a percentage."""
    disk = psutil.disk_usage(path)
    return disk.percent

def main():
    print("Gathering system metrics")
    
    cpu = get_cpu_usage()
    ram = get_memory_usage()
    disk = get_disk_usage()
    
    print(f"CPU Usage:  {cpu}%")
    print(f"RAM Usage:  {ram}%")
    print(f"Disk Usage: {disk}%")

if __name__ == "__main__":
    main()