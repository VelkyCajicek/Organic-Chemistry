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

        self.canvas = tk.Canvas(self.root, height=400, width=800)
        self.canvas.pack()
        self.t = turtle.RawTurtle(self.canvas)

    def RunTestCases(self, t : turtle.RawTurtle) -> None:
        with open("testCases.txt", "r") as data:
            lines = [line.strip() for line in data]

        lines = list(filter(lambda a: a[0] != "#", lines)) # Removes titles

        for compound in lines:
            t.reset()
            self.confirmButton.config(text=compound)
            try:
                compoundData, bondPositions = mainFormula(compound.strip().lower())
                self.DrawAlkanesSimple(t, len(compoundData), compoundData, bondPositions)
                time.sleep(1)
            except(IndexError):
                print(compound)

        self.confirmButton.config(text="Confirm")

    def main(self, t : turtle.RawTurtle) -> None:
        t.reset() # Resets the canvas
        if(self.userInputBox.get() == "run"):
            self.RunTestCases(t)
        else:
            compoundData, bondPositions = mainFormula(self.userInputBox.get().strip().lower()) # White spaces are very bad
            self.DrawAlkanesSimple(t, len(compoundData), compoundData, bondPositions)

    def DrawHydrocarbonResidue(self, currentAngle : float, t : turtle.RawTurtle, compoundDataElement : int):
        currentPosX = t.xcor()
        currentPosY = t.ycor()
        t.setheading(90 + currentAngle)
        t.forward(30)
        t.left(30)
        for _ in range(0, compoundDataElement - 1):
            if(t.heading() == 120.0 + currentAngle): # This doesnt yet work so currentAngle will be set to 0
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
        if(bondPositions[i] != 0):
            if(bondPositions[i] == 2):
                t.pencolor("red")
            if(bondPositions[i] == 3):
                t.pencolor("green")

    def DrawAlkanesSimple(self, t : turtle.RawTurtle, mainCarbonCount : int, compoundData : list, bondPositions : list) -> None:
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

if __name__ == "__main__":
    myGUI = GUI()