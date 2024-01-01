from kivy.config import Config

Config.set("graphics", "height", "600")
Config.set("graphics", "width", "400")
Config.set("graphics", "resizable", "0")
Config.set('input', 'mouse', 'mouse,disable_multitouch')

from kivymd.app import MDApp
from kivy.properties import ListProperty
from api import MainWindow


class ColorSelectorApp(MDApp):
    color = ListProperty([0.0253,0.6139,1.0,1.0])
    changed_color = ListProperty([0,0,0,0])

    def __init__(self, **kwargs):
        super(ColorSelectorApp, self).__init__(**kwargs)
        self.title = "Color Selector"
        self.icon = "asset/data/ibgs"

    def build(self):
        return MainWindow()

    def rgba_to_hex(self,info):
        local_list = []
        for float_val in info:
            hex_val = int(float_val * 255)
            local_list.append(f"{hex_val:02x}")
        r,g,b,a = local_list
        return f"#{r}{g}{b}"


if __name__ == '__main__':
    window = ColorSelectorApp()
    window.icon = "icon.ico"
    try:
        with open("asset/data/ibgs", "rb") as data:
            window.run()
    except:
        pass
