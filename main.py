import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class CreepDetection():
    ''' Class responsible for the sound recognition functionlaity '''
    def __init__(self):
        pass

    @classmethod
    def detectCreep(self):
        pass


class MyGrid(Widget):
    button = ObjectProperty(None)
    pressed = False

    def btn(self):
        self.pressed = not self.pressed
        # if active
        if self.pressed:
            self.button.text = "Stop"
            CreepDetection.detectCreep()
        else:
            self.button.text = "Start"



class MyApp(App):  # <- Main Class
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
