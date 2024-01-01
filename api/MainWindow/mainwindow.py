from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder

Builder.load_string("""
<MainWindow>
    padding:[10]
    orientation:"vertical"
    spacing:10
    
    ColorDisplay:
    CopyColorValues:
    ShowTheColor:
    
""")


class MainWindow(MDBoxLayout):
    pass
