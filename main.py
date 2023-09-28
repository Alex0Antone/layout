from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.widget import Widget
from kivy.uix.button import Button
class GridLayoutExample(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        for letter in "0123456789abcdefgh":
            b = Button(text="Button "+letter.upper(),  background_color=(0, 1, .1))
            self.add_widget(b)


class LayoutAssignment(BoxLayout):
    pass
class StackLayoutExample(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for letter in "abcdefghijklmnopqrstuvwxyz0123456789":
            b = Button(text ="Button "+ letter.upper())
            self.add_widget(b)
class BoxLayoutExample(BoxLayout):
    pass
class MainWidget(Widget):
    pass

class WidgetLayoutApp(App):
    pass

WidgetLayoutApp().run()
