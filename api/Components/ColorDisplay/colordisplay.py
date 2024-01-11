from kivymd.uix.boxlayout import MDBoxLayout
from kivy.properties import NumericProperty
from kivy.lang.builder import Builder

Builder.load_string("""
<ColorDisplay>
    app:app
    adaptive_height:True
    GridLayout:
        canvas.before:
            Color:
                rgba:app.color
            RoundedRectangle:
                size:self.size
                pos:self.pos
                radius:[10]
        cols:2
        row_force_default:True
        row_default_height:40
        size_hint_y:None
        height:self.row_default_height*4
        MDLabel:
            text:"R"
            halign:"center"
        Slider:
            id:slider_r
            max:1.0
            min:0.0
            #value_track_color:[1,1,0,1]
            cursor_height:root.cursur_size
            cursor_width:root.cursur_size
            on_value:app.changed_color[0] = self.value
            
        MDLabel:
            text:"G"
            halign:"center"
        Slider:
            id:slider_g
            max:1.0
            min:0.0
            #value_track_color:[1,1,0,1]
            cursor_height:root.cursur_size
            cursor_width:root.cursur_size
            on_value:app.changed_color[1] = self.value
            
        MDLabel:
            text:"B"
            halign:"center"
        Slider:
            id:slider_b
            max:1.0
            min:0.0
            #value_track_color:[1,1,0,1]
            cursor_height:root.cursur_size
            cursor_width:root.cursur_size
            on_value:app.changed_color[2] = self.value
            
        MDLabel:
            text:"A"
            halign:"center"
        Slider:
            id:slider_a
            max:1.0
            min:0.0
            #value_track_color:[1,1,0,1]
            cursor_height:root.cursur_size
            cursor_width:root.cursur_size
            on_value:app.changed_color[3] = self.value
            

""")

class ColorDisplay(MDBoxLayout):
    r_val = NumericProperty()
    g_val = NumericProperty()
    b_val = NumericProperty()
    a_val = NumericProperty()
    cursur_size = NumericProperty(26)
