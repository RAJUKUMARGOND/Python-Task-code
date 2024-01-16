import requests

def get_public_ip():
    try:
        # Use a service like ipinfo.io to fetch the public IP address
        response = requests.get('https://ipinfo.io')
        data = response.json()
        
        # Extract the public IP address from the response
        public_ip = data.get('ip')
        
        if public_ip:
            return public_ip
        else:
            raise Exception("Public IP address not found in the response")
    except requests.exceptions.RequestException as req_err:
        raise Exception(f"Request error occurred: {req_err}")
    except Exception as e:
        raise Exception(f"Failed to retrieve public IP address: {e}")

if __name__ == "__main__":
    try:
        public_ip = get_public_ip()
        print(f"Public IP Address: {public_ip}")
    except Exception as e:
        print(f"An error occurred: {e}")

