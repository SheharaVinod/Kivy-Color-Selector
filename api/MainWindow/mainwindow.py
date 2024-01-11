from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang.builder import Builder

Builder.load_string("""
<MainWindow>
    padding:[10]
    orientation:"vertical"
    spacing:10
    #md_bg_color:[0,0,1,0.8]
    #adaptive_height:True
    
    ColorDisplay:
    CopyColorValues:
    ShowTheColor:
    
""")


class MainWindow(MDBoxLayout):
    pass
