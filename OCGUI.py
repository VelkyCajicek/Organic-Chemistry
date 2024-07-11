import tkinter as tk 
import turtle
import time

from formula import mainFormula

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

        lines = list(filter(lambda a: a[0] != "#", lines)) # Removes titles

        for compound in lines:
            t.reset()
            self.confirmButton.config(text=compound)
            try:
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
        elif(self.userInputBox.get() == "test"):
            compoundData = [0, 0, 2, 2, [3, 3], 0, 0, 0, 0]
            bondPositions = [2, 1, 1, 1, 1, 2, 1, 1, 1]
        else:
            compoundData, bondPositions = mainFormula(self.userInputBox.get().strip().lower().replace("cyklo", "")) 
            if(self.switchButton.cget("text") == "Simple"):
                self.DrawHydrocarbonSimple(t, len(compoundData), compoundData, bondPositions)
            else:
                self.DrawHydroCarbonComplex(t, len(compoundData), compoundData, bondPositions)

    def DrawHydroCarbonComplex(self, t : turtle.RawTurtle, mainCarbonCount : int, compoundData : list, bondPositions : list):
        # First calculate a position to center the formula (turtle starts at coords 0,0)
        t.penup()
        t.goto(len(compoundData) * -25, t.ycor()) # Rough calculation that should do the trick for now
        
        t.write(self.CalculateHydrogens(compoundData, 0), font=("Arial", 14, "normal"))
        for i in range(1, mainCarbonCount - 1):
            t.forward(10)
            t.goto(t.xcor() + 20, t.ycor() + 7)
            t.pendown()
            if(bondPositions[i] == 2):
                t.color("red")
            if(bondPositions[i] == 3):
                t.color("blue")
            t.forward(25)
            t.color("black")
            t.penup()
            t.goto(t.xcor() - 20, t.ycor() - 7)
            t.forward(25)
            t.write(self.CalculateHydrogens(compoundData, i), font=("Arial", 14, "normal"))
            if(compoundData[i] != 0):
                if(type(compoundData[i]) is list):
                    self.DrawHydrocarbonResidueComplex(t, compoundData, compoundData[i][0], 90)
                    self.DrawHydrocarbonResidueComplex(t, compoundData, compoundData[i][1], 270)
                else:
                    self.DrawHydrocarbonResidueComplex(t, compoundData, compoundData[i], 90)

    def CalculateHydrogens(self, compoundData : list, i : int) -> str:
        hydrogenCount = 4 # Carbon is "čtyřvazný"
        if(i != 0 or i != len(compoundData) - 1):
            hydrogenCount -= 1
        if(compoundData[i] != 0):
            hydrogenCount -= 1
        if(type(compoundData[i]) == list):
            hydrogenCount -= 1
        return f"CH{hydrogenCount}".replace("H0", "").replace("1", "")

    def DrawHydrocarbonResidueComplex(self, t : turtle.RawTurtle, compoundData : list, compoundDataElement : int, heading : int) -> None:
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
            t.write(self.CalculateHydrogens(compoundData, i), font=("Arial", 14, "normal"))

        t.setheading(0)
        t.goto(currentPosX, currentPosY)

    def DrawHydrocarbonResidue(self, currentAngle : float, t : turtle.RawTurtle, compoundDataElement : int):
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

    def DrawAdditionalInfo(self, rotation : int, compoundData : list, i : int, bondPositions : list, t : turtle.RawTurtle) -> None:
        if(compoundData[i] != 0): # These parts just mean that it draws so residue part and then continues drawing the backbone
            if(type(compoundData[i]) is list):
                self.DrawHydrocarbonResidue(0, t, compoundData[i][0])
                self.DrawHydrocarbonResidue(180, t, compoundData[i][1])
            else:
                self.DrawHydrocarbonResidue(0, t, compoundData[i])
            t.setheading(rotation)
        if(bondPositions[i] != 1):
            if(bondPositions[i] == 2):
                t.pencolor("red")
            if(bondPositions[i] == 3):
                t.pencolor("blue")

    def DrawHydrocarbonSimple(self, t : turtle.RawTurtle, mainCarbonCount : int, compoundData : list, bondPositions : list) -> None:
        t.penup()
        t.goto(len(compoundData) * -10, t.ycor()) # -10 seems like it works well (sets the initial position so its centered)
        t.pendown()

        t.left(30)
        for i in range(0, mainCarbonCount - 1): # -1 since each end point is a carbon
            if(t.heading() == 30.0):
                self.DrawAdditionalInfo(30, compoundData, i, bondPositions, t)
                t.forward(30)
                t.right(60)
                t.pencolor("black")
            else:
                self.DrawAdditionalInfo(330, compoundData, i, bondPositions, t)
                t.forward(30)
                t.left(60)
                t.pencolor("black")
        time.sleep(0.5)

    def DrawCyclicalHydrocarbon(self, t : turtle.RawTurtle, mainCarbonCount : int, compoundData : list, bondPositions : list):
        for i in range(0, mainCarbonCount):
            self.DrawAdditionalInfo(30, compoundData, i, bondPositions, t)
            t.forward(30)
            t.left(360 / mainCarbonCount)

if __name__ == "__main__":
    myGUI = GUI()