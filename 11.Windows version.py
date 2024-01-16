import platform

def get_windows_version():
    try:
        # Get the Windows version information
        windows_version = platform.system() + " " + platform.version()

        return windows_version

    except Exception as e:
        return f"Error fetching Windows version: {str(e)}"

# Example usage
windows_version = get_windows_version()
print(f"Windows Version: {windows_version}")