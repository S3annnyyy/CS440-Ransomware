import ctypes
import os
import sys

def resource_path(relative_path):
    """ This function gets the absolute path to resource"""
    try:        
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
        print(base_path, relative_path)


    return os.path.join(base_path, relative_path)


def change_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)
wallpaper = resource_path("img/windows.jpg")

change_wallpaper(wallpaper)