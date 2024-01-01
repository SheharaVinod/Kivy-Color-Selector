from kivy.lang.builder import Builder
from kivymd.uix.boxlayout import MDBoxLayout

Builder.load_string("""
<CopyColorValues>
    app:app
    md_bg_color:app.color
    radius:10
    orientation:"vertical"
    size_hint_y:None
    height:child_grid.row_default_height*2.5 + 10
    
    GridLayout:
        id:child_grid
        cols:2
        row_force_default:True
        row_default_height:30
        spacing:5
        padding:[10]
        
        MDLabel:
            text:"From List"
            halign:"center"
            size_hint_x:None
            width:100
        TextInput:
            text:"[{},{},{},{}]".format(round(app.changed_color[0],5),\
                                        round(app.changed_color[1],5),\
                                        round(app.changed_color[2],5),\
                                        round(app.changed_color[3],5))
        
        MDLabel:
            text:"From Hex"
            halign:"center"
            size_hint_x:None
            width:100
        TextInput:
            text: app.rgba_to_hex(app.changed_color)
            
            


""")

class CopyColorValues(MDBoxLayout):
    pass
