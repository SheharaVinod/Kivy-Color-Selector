from kivy.config import Config

Config.set("graphics", "height", "600")
Config.set("graphics", "width", "400")
Config.set("graphics", "resizable", "0")
Config.set('input', 'mouse', 'mouse,disable_multitouch')
Config.set('kivy', 'exit_on_escape', "0")

from kivymd.app import MDApp
from kivy.properties import ListProperty
from api import MainWindow
from kivy import *
from kivymd import *
from os.path import exists


class ColorSelectorApp(MDApp):
    color = ListProperty([0.0253, 0.6139, 1.0, 1.0])
    changed_color = ListProperty([0, 0, 0, 0])

    def __init__(self, **kwargs):
        super(ColorSelectorApp, self).__init__(**kwargs)
        self.title = "Color Selector"
        self.icon = "asset/data/icon.png"

    def build(self):
        return MainWindow()

    def rgba_to_hex(self, info):
        local_list = []
        for float_val in info:
            hex_val = int(float_val * 255)
            local_list.append(f"{hex_val:02x}")
        r, g, b, a = local_list
        return f"#{r}{g}{b}"

    def open_settings(self, *largs):
        # for pass F1 Setting screen.
        pass


if __name__ == '__main__':
    window = ColorSelectorApp()

    is_exist = True
    all_files = [
        "asset/data/icon.png",
        "asset/image/Back.jpg",
        "asset/image/icon.ico",
        "asset/image/icon.png",
        "icon.ico"
    ]
    for each_file in all_files:
        if exists(each_file):
            continue
        else:
            is_exist = False
    if is_exist:
        window.run()
