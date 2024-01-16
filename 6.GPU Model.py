import GPUtil

def get_gpu_info():
    try:
        # Get a list of GPU devices
        gpus = GPUtil.getGPUs()

        if gpus:
            # Assuming the first GPU in the list is the primary one
            gpu_model = gpus[0].name
            return gpu_model
        else:
            return "No GPU detected."

    except Exception as e:
        return f"Error fetching GPU information: {str(e)}"

# Example usage
gpu_model = get_gpu_info()
print(f"GPU Model: {gpu_model}")
