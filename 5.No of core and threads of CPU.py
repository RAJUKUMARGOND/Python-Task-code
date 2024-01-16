import psutil

def get_cpu_info():
    # Get the number of physical cores
    physical_cores = psutil.cpu_count(logical=False)
    
    # Get the total number of logical cores (including hyper-threading threads)
    logical_cores = psutil.cpu_count(logical=True)

    return physical_cores, logical_cores

# Example usage
physical_cores, logical_cores = get_cpu_info()

print(f"Number of Physical Cores: {physical_cores}")
print(f"Number of Threads (Logical Cores): {logical_cores}")