import tkinter as tk 
import turtle
import time

from formula import mainFormula

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

        self.canvas = tk.Canvas(self.root, height=400, width=800)
        self.canvas.pack()
        self.t = turtle.RawTurtle(self.canvas)

    def updateSwitch(self) -> None: 
        if(self.switchButton.cget("text") == "Simple"): # This has proved to work
            self.switchButton.config(text="Complex")
        else:
            self.switchButton.config(text="Simple")

    def RunTestCases(self, t : turtle.RawTurtle) -> None:
        with open("testCases.txt", "r") as data:
            lines = [line.strip() for line in data]

        lines = list(filter(lambda a: a[0] != "#", lines)) # Removes titles (index for cyclical is 18)

        for compound in lines: 
            t.reset()
            self.confirmButton.config(text=compound)
            try:
                if("cyklo" in compound):
                    compoundData, bondPositions = mainFormula(compound.strip().lower().replace("cyklo", "")) 
                    self.DrawCyclicalHydrogen(t, len(compoundData), compoundData, bondPositions)
                else:
                    compoundData, bondPositions = mainFormula(compound.strip().lower()) 
                    if(self.switchButton.cget("text") == "Simple"):
                        self.DrawHydrocarbonSimple(t, len(compoundData), compoundData, bondPositions)
                    else:
                        self.DrawHydroCarbonComplex(t, len(compoundData), compoundData, bondPositions)
            except(IndexError):
                print(compound)

        self.confirmButton.config(text="Confirm")

    def main(self, t : turtle.RawTurtle) -> None:
        t.reset() # Resets the canvas

        if(self.userInputBox.get() == "run"):
            self.RunTestCases(t)
        else:
            if("cyklo" in self.userInputBox.get()):
                compoundData, bondPositions = mainFormula(self.userInputBox.get().strip().lower().replace("cyklo", "")) 
                self.DrawCyclicalHydrogen(t, len(compoundData), compoundData, bondPositions)
            else:
                compoundData, bondPositions = mainFormula(self.userInputBox.get().strip().lower()) 
                if(self.switchButton.cget("text") == "Simple"):
                    self.DrawHydrocarbonSimple(t, len(compoundData), compoundData, bondPositions)
                else:
                    self.DrawHydroCarbonComplex(t, len(compoundData), compoundData, bondPositions)

    def DrawBonds(self, t : turtle.RawTurtle, numBonds : int) -> None:
        currentPosX = t.xcor()
        currentPosY = t.ycor()
        t.forward(30) # This is for the main one
        finalPosX = t.xcor()
        finalPosY = t.ycor()
        if(numBonds == 2):
            t.penup()
            t.goto(currentPosX, currentPosY - 5)
            t.pendown()
            t.forward(30)
        if(numBonds == 3):
            t.penup()
            t.goto(currentPosX, currentPosY - 5)
            t.pendown()
            t.forward(30)
            t.penup()
            t.goto(currentPosX, currentPosY + 5)
            t.pendown()
            t.forward(30)
        t.penup()
        t.goto(finalPosX, finalPosY)
        t.pendown()

    # Complex code here

    def DrawHydroCarbonComplex(self, t : turtle.RawTurtle, mainCarbonCount : int, compoundData : list, bondPositions : list) -> None:
        # First calculate a position to center the formula (turtle starts at coords 0,0)
        t.penup()
        t.goto(len(compoundData) * -25, t.ycor()) # Rough calculation that should do the trick for now
        
        t.write(self.CalculateHydrogens(compoundData, 0, bondPositions), font=("Arial", 14, "normal")) # This logic is incorrect
        for i in range(1, mainCarbonCount):
            t.forward(10) # This doesnt seem to draw
            t.goto(t.xcor() + 20, t.ycor() + 7)
            t.pendown()
            self.DrawBonds(t, bondPositions[i])
            t.penup()
            t.goto(t.xcor() - 20, t.ycor() - 7)
            t.forward(25)
            t.write(self.CalculateHydrogens(compoundData, i, bondPositions), font=("Arial", 14, "normal"))
            if(compoundData[i] != 0):
                if(type(compoundData[i]) is list):
                    self.DrawHydrocarbonResidueComplex(t, compoundData, compoundData[i][0], 90, bondPositions)
                    self.DrawHydrocarbonResidueComplex(t, compoundData, compoundData[i][1], 270, bondPositions)
                else:
                    self.DrawHydrocarbonResidueComplex(t, compoundData, compoundData[i], 90, bondPositions)
        time.sleep(0.5)

    def CalculateHydrogens(self, compoundData : list, i : int, bondPositions : list) -> str:
        hydrogenCount = 3 # Carbon is "čtyřvazný"
        if(i != 0):
            hydrogenCount -= 1
        if(compoundData[i] != 0):
            hydrogenCount -= 1
        if(type(compoundData[i]) is list):
            hydrogenCount -= 1
        if(bondPositions[i] == 2):
            hydrogenCount -= 1
        if(bondPositions[i] == 3):
            hydrogenCount -= 2  
        return f"CH{hydrogenCount}".replace("H0", "").replace("1", "")

    def DrawHydrocarbonResidueComplex(self, t : turtle.RawTurtle, compoundData : list, compoundDataElement : int, heading : int, bondPositions : list) -> None:
        multiplier = 1 # This is if the residue is going to be going down
        currentPosX = t.xcor()
        currentPosY = t.ycor()

        t.penup()
        t.setheading(heading)

        if(heading == 270):
            multiplier = -1

        for i in range(0, compoundDataElement): # This is not perfect, may require 2 for loops in a if else statement
            t.goto(t.xcor() + 7, t.ycor() + 20 * multiplier)
            t.pendown()
            t.forward(25)
            t.penup()
            t.goto(t.xcor() - 7, t.ycor() - 20 * multiplier)
            if(heading == 270):
                t.forward(15)
            t.forward(25)
            t.write(self.CalculateHydrogens(compoundData, i, bondPositions), font=("Arial", 14, "normal"))

        t.setheading(0)
        t.goto(currentPosX, currentPosY)

    # Simple code here

    def DrawHydrocarbonResidue(self, currentAngle : float, t : turtle.RawTurtle, compoundDataElement : int): # This needs reworking
        currentPosX = t.xcor()
        currentPosY = t.ycor()
        t.setheading(90 + currentAngle)
        t.forward(30)
        t.left(30)
        for _ in range(0, compoundDataElement - 1):
            if(t.heading() == 120.0 + currentAngle): 
                t.forward(30)
                t.right(60) 
            else:
                t.forward(30)
                t.left(60)
        t.penup()
        t.goto(currentPosX, currentPosY) # Resets position
        t.pendown()

    def DrawAdditionalInfo(self, compoundData : list, i : int, t : turtle.RawTurtle) -> None:
        currentHeading = t.heading()
        if(compoundData[i] != 0): # These parts just mean that it draws so residue part and then continues drawing the backbone
            if(type(compoundData[i]) is list):
                self.DrawHydrocarbonResidue(0, t, compoundData[i][0])
                self.DrawHydrocarbonResidue(180, t, compoundData[i][1])
            else:
                self.DrawHydrocarbonResidue(0, t, compoundData[i])
        t.setheading(currentHeading)

    def DrawHydrocarbonSimple(self, t : turtle.RawTurtle, mainCarbonCount : int, compoundData : list, bondPositions : list) -> None:
        t.penup()
        t.goto(len(compoundData) * -10, t.ycor()) # -10 seems like it works well (sets the initial position so its centered)
        t.pendown()

        t.left(30)
        for i in range(0, mainCarbonCount - 1): # -1 since each end point is a carbon
            if(t.heading() == 30.0):
                self.DrawAdditionalInfo(compoundData, i, t)
                self.DrawBonds(t, bondPositions[i])
                t.right(60)
            else:
                self.DrawAdditionalInfo(compoundData, i, t) # Residue
                self.DrawBonds(t, bondPositions[i]) # Bonds
                t.left(60)
        time.sleep(0.5)

    # Cyclical code here

    def DrawCyclicalHydrogen(self, t : turtle.RawTurtle, mainCarbonCount : int, compoundData : list, bondPositions : list):
        for i in range(0, mainCarbonCount):
            self.DrawCyclicalHydrogenAdditionalInfo(compoundData, i, t)
            self.DrawBonds(t, bondPositions[i])
            t.left(360 / mainCarbonCount)
        time.sleep(0.5)

    def DrawHydrocarbonResidueCyclical(self, currentAngle : float, t : turtle.RawTurtle, compoundDataElement : int): # This needs reworking
        currentPosX = t.xcor()
        currentPosY = t.ycor()
        t.right(currentAngle)
        rotation = t.heading()
        for _ in range(0, compoundDataElement):
            if(t.heading() == rotation): 
                t.forward(30)
                t.right(60) 
            else:
                t.forward(30)
                t.left(60)
        t.penup()
        t.goto(currentPosX, currentPosY) # Resets position
        t.pendown()

    def DrawCyclicalHydrogenAdditionalInfo(self, compoundData : list, i : int, t : turtle.RawTurtle):
        currentHeading = t.heading()
        if(compoundData[i] != 0): # These parts just mean that it draws so residue part and then continues drawing the backbone
            if(type(compoundData[i]) is list):
                self.DrawHydrocarbonResidueCyclical(180 / len(compoundData), t, compoundData[i][0])
                self.DrawHydrocarbonResidueCyclical(360 / len(compoundData), t, compoundData[i][1])
            else:
                self.DrawHydrocarbonResidueCyclical(t.heading() - 360 / len(compoundData), t, compoundData[i])
        t.setheading(currentHeading)

if __name__ == "__main__":
    myGUI = GUI()