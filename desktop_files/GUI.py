import tkinter as tk 
import turtle
import re

from formula import mainFormula
from hydrocarbon_derivatives import *
from canvasShapes import DraggableShapes

from drawing_scripts.simple_hydrocarbon import SimpleHydrocarbon
from drawing_scripts.cyclical_hydrocarbon import CyclicalHydrocarbon
from drawing_scripts.complex_hydrocarbon import ComplexHydrocarbon

# For complex compounds the distance is the same as simple for the bonds !!!

class GUI:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.initialize()
        self.root.mainloop()

    def initialize(self) -> None:
        self.root.title("Organic Chemistry")
        self.root.geometry("800x800")

        self.userInputBox = tk.Entry(self.root)
        self.userInputBox.pack()

        self.confirmButton = tk.Button(self.root, text="Confirm", command= lambda : self.main(self.t))
        self.confirmButton.pack()

        self.switchButton = tk.Button(self.root, text="Simple", command= lambda : self.updateSwitch())
        self.switchButton.pack()
        
        self.breakButton = tk.Button(self.root, text="Break", command= lambda : self.breakButton.config(text="Cancelling"))
        self.breakButton.pack()

        self.canvas = tk.Canvas(self.root, height=400, width=800)
        self.canvas.pack()
        self.t = turtle.RawTurtle(self.canvas)
        self.canvasInteraction = DraggableShapes(self.canvas)
        
        self.s = SimpleHydrocarbon()
        self.cy = CyclicalHydrocarbon()
        self.co = ComplexHydrocarbon()
    
    def updateSwitch(self) -> None: 
        if(self.switchButton.cget("text") == "Simple"): # This has proved to work
            self.switchButton.config(text="Complex")
        else:
            self.switchButton.config(text="Simple")

    def formatUserInput(self, userInput : str) -> str:
        # Check for special type of ligand in compound
        for compound in AromaticCompounds:
            if(compound.name in userInput):
                if(compound.name == userInput):
                    userInput = userInput.replace(compound.name, compound.formula)
                else:
                    userInput = userInput.replace(compound.name, f"-{compound.formula}")

        return userInput.replace("--", "-")

    def main(self, t : turtle.RawTurtle) -> None:
        t.reset() # Resets the canvas

        if(self.userInputBox.get() == "run"):
            self.RunTestCases(t)
        elif(self.userInputBox.get() == "test"):
            self.DrawNaphthalene(t)
        else:
            # Check for special type of ligand in compound
            userInput = self.formatUserInput(self.userInputBox.get())

            digitCheck = re.compile(r"\d") # This is mostly for cyclical formulas since if there is no num at the beggining it assigns the residue to the first one
            if(not digitCheck.match(userInput[0])):
                userInput = "1-" + userInput

            # Draw the compound
            if("cyklo" in userInput):
                compoundData, bondPositions = mainFormula(userInput.strip().lower().replace("cyklo", "")) 
                self.cy.DrawCyclicalHydrogen(t, len(compoundData), compoundData, bondPositions)
            else:
                compoundData, bondPositions = mainFormula(userInput.strip().lower()) 
                if(self.switchButton.cget("text") == "Simple"):
                    self.s.DrawHydrocarbonSimple(t, len(compoundData), compoundData, bondPositions)
                else:
                    self.co.DrawHydroCarbonComplex(t, len(compoundData), compoundData, bondPositions)

    # Testing
    def DrawNaphthalene(self, t : turtle.RawTurtle, compoundData : list):
        t.setheading(30)
        for i in range(0, 5):
            if(i % 2 == 0):
                self.DrawBonds(t, 2, t.heading())
            else:
                self.DrawBonds(t, 1, t.heading())
            t.right(60)
        t.setheading(210)
        for i in range(5, 11):
            if(i % 2 == 0):
                self.DrawBonds(t, 1, t.heading())
            else:
                self.DrawBonds(t, 2, t.heading())
            t.right(60)

    # Testing

    def RunTestCases(self, t : turtle.RawTurtle) -> None:
        with open("testCases.txt", "r") as data:
            lines = [line.strip() for line in data]

        lines = list(filter(lambda a: a[0] != "#", lines)) # Removes titles (index for cyclical is 18)

        lines = lines[40:]

        for compound in lines: 
            t.reset()
            if(self.breakButton.cget("text") == "Cancelling"): # Cancel the run script
                self.breakButton.config(text="Break")
                break
            self.confirmButton.config(text=compound)
            try:
                breakCheck = False # This may or may not be better since it allows the program to skip the code below the breakCheck check
                compound = self.formatUserInput(compound)
                for derivative in HydrocarbonDerivativeList:
                    if(derivative.preffix in compound):               
                        breakCheck = True
                        if("cyklo" in compound):
                            compoundData, bondPositions = mainFormula(compound.strip().lower().replace("cyklo", "")) 
                            self.cy.DrawCyclicalHydrogen(t, len(compoundData), compoundData, bondPositions)
                        else:
                            previousState = self.switchButton.cget("text")
                            self.switchButton.config(text="Complex")
                            self.co.DrawHydroCarbonComplex(t, len(compoundData), compoundData, bondPositions)
                            self.switchButton.config(text=previousState)
                        break
                if(breakCheck):
                    continue
                if("cyklo" in compound):
                    compoundData, bondPositions = mainFormula(compound.strip().lower().replace("cyklo", "")) 
                    self.cy.DrawCyclicalHydrogen(t, len(compoundData), compoundData, bondPositions)
                else:
                    compoundData, bondPositions = mainFormula(compound.strip().lower())
                    if(self.switchButton.cget("text") == "Simple"):
                        self.s.DrawHydrocarbonSimple(t, len(compoundData), compoundData, bondPositions)
                    else:
                        self.co.DrawHydroCarbonComplex(t, len(compoundData), compoundData, bondPositions)
            except(IndexError):
                print(compound)

        self.confirmButton.config(text="Confirm")

if __name__ == "__main__":
    myGUI = GUI()