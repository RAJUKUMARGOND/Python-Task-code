import pygetwindow as gw

def get_screen_size():
    try:
        # Get the primary screen
        primary_screen = gw.getWindowsWithTitle('')[0]

        # Get the screen width and height
        screen_width, screen_height = primary_screen.width, primary_screen.height

        return screen_width, screen_height

    except Exception as e:
        return f"Error fetching screen size: {str(e)}"

# Example usage
screen_width, screen_height = get_screen_size()
print(f"Screen Size: {screen_width}x{screen_height} pixels")