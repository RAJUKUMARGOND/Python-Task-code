import psutil

def get_ram_size():
    try:
        # Get the virtual memory (RAM) information
        ram_info = psutil.virtual_memory()

        # Convert the RAM size to GB
        ram_size_gb = ram_info.total / (1024**3)

        return ram_size_gb

    except Exception as e:
        return f"Error fetching RAM information: {str(e)}"

# Example usage
ram_size = get_ram_size()
print(f"RAM Size: {ram_size:.2f} GB")
