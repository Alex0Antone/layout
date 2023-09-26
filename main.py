from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
class GridLayoutExample(GridLayout):
    pass

class LayoutAssignment(BoxLayout):
    pass
class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for letter in "abcdefghijklmnopqrstuvwxyz0123456789":
            b = Button(text ="Button "+ letter.upper(), size_hint=(.2, .2))
            self.add_widget(b)
class BoxLayoutExample(BoxLayout):
    pass
class MainWidget(Widget):
    pass

class WidgetLayoutApp(App):
    pass

WidgetLayoutApp().run()
