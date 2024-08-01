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
from tivy import Tivy
from formula import mainFormula

class ChemistyLogic:
    def DrawBonds(self, t : Tivy, numBonds : int) -> None:
        if(numBonds == 2):
            Color(255, 0, 0, 0.5)
        if(numBonds == 3):
            Color(255, 0, 0, 0.5)
        t.foward(30)
        Color()

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
        self.bondPositions = []
        self.compoundData = []
        self.t.setpos(250, 250) # These two lines could be temporary
        self.t.setheading(30)

        with self.canvas:
            info = self.DrawHydrocarbonSimple(len(self.compoundData))
            Line(points=info, width=1)
        
    def on_enter(self, event): # event here means that it registers a click
        self.compoundData, self.bondPositions = mainFormula(str(self.textInput.text).strip().lower().replace("cyklo", ""))

    def DrawHydrocarbonSimple(self, mainCarbonCount : int) -> list:
        formulaInfo = []
        for i in range(0, mainCarbonCount - 1):
            if(self.t.heading() == 30.0):
                formulaInfo.extend(self.t.currentPosition)
                self.t.setheading(330)
            else:
                formulaInfo.extend(self.t.currentPosition)
                self.t.setheading(30)
            self.t.foward(30)
        return formulaInfo
        
class KivyCanvas(App):
    def build(self):
        return MainRelativeLayout()
    
if __name__ == "__main__":
    window = KivyCanvas()
    window.run()