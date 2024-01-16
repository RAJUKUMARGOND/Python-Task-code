import win32api

screen_width = win32api.GetSystemMetrics(0)
screen_height = win32api.GetSystemMetrics(1)


print("Screen Resolution: {}x{}".format(screen_width, screen_height))