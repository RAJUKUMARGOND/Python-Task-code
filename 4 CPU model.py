import platform

def get_cpu_model():
    try:
        # Fetch CPU model using platform module
        cpu_model = platform.processor()
        return cpu_model
    except Exception as e:
        raise Exception(f"Failed to retrieve CPU model: {e}")

if __name__ == "__main__":
    try:
        cpu_model = get_cpu_model()
        print(f"CPU Model: {cpu_model}")
    except Exception as e:
        print(f"An error occurred: {e}")
