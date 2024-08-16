# Minimum requirements
import kivy
from kivy.app import App
kivy.require("1.9.0")
# Canvas related imports
from kivy.uix.widget import Widget
from kivy.graphics import *
# Additional widgets
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
# Resolution and positional imports
from kivy.uix.stacklayout import StackLayout
from kivy.core.window import Window
Window.size = (71.5*8, 146.7*3.5)
# App functionality imports from different personal scripts
from drawing_scripts.tivy import Tivy
from drawing_scripts.simple_hydrocarbon import SimpleHydrocarbon
from formula import mainFormula

class MainRelativeLayout(StackLayout):
    def __init__(self, **kw):
        super(MainRelativeLayout, self).__init__(**kw)
        # Still a bit unsure what this super is
        self.textInput = TextInput(size_hint_y=0.1, size_hint_x=1) # Size hint is from 0 to 1 and x is to align on x axis 
        self.confirmButton = Button(text="Convert", size_hint_y=0.1, size_hint_x=1)
        # Add widget seems to add the widget to the app
        self.add_widget(self.textInput)
        self.add_widget(self.confirmButton)
        self.confirmButton.bind(on_press=self.on_enter)
        # App logic
        self.t = Tivy()
        self.s = SimpleHydrocarbon()
        self.bondPositions = []
        self.compoundData = []

        #compoundData = [0, 0, 2, 2, [3, 3], 0, 0, 0, 0]
        #bondPositions = [2, 1, 1, 1, 1, 2, 1, 1, 1]

        #with self.canvas:
        #    self.s.DrawHydrocarbonSimple(self.t, len(compoundData), compoundData, bondPositions)
        
    def on_enter(self, event): # event here means that it registers a click
        self.canvas.clear()
        if(str(self.textInput.text) == "run"):
            with open("testCases.txt", "r") as data:
                lines = [line.strip() for line in data]

            lines = list(filter(lambda a: a[0] != "#", lines)) # Removes titles (index for cyclical is 18)

        else:
            compoundData, bondPositions = mainFormula(str(self.textInput.text).strip().lower().replace("cyklo", ""))
            with self.canvas:
                self.s.DrawHydrocarbonSimple(self.t, len(compoundData), compoundData, bondPositions)

class KivyCanvas(App):
    def build(self):
        return MainRelativeLayout()
    
if __name__ == "__main__":
    window = KivyCanvas()
    window.run()