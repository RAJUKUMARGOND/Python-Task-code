import psutil

def get_mac_addresses():
    try:
        # Get network interfaces information
        network_info = psutil.net_if_addrs()

        # Initialize variables to store MAC addresses
        wifi_mac = None
        ethernet_mac = None

        # Iterate through network interfaces
        for interface, addresses in network_info.items():
            for address in addresses:
                # Check if the address corresponds to a MAC address and matches Wi-Fi or Ethernet
                if address.family == psutil.AF_LINK:
                    if 'Wi-Fi' in interface:
                        wifi_mac = address.address
                    elif 'Ethernet' in interface:
                        ethernet_mac = address.address

        return wifi_mac, ethernet_mac

    except Exception as e:
        return f"Error fetching MAC addresses: {str(e)}"

# Example usage
wifi_mac_address, ethernet_mac_address = get_mac_addresses()
print(f"Wi-Fi MAC Address: {wifi_mac_address}")
print(f"Ethernet MAC Address: {ethernet_mac_address}")