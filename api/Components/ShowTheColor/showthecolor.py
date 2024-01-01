from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_string("""
<ShowTheColor>
    app:app
    canvas.after:
        Color:
            rgba:app.changed_color
        RoundedRectangle:
            size:self.size
            pos:self.pos
    radius:10
    size_hint_y:None
    height:275
    FitImage:
        source:"asset/image/Back.jpg"
        radius:10
""")

class ShowTheColor(MDBoxLayout):
    pass