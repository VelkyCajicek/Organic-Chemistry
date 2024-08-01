import time
import turtle

class ComplexHydrocarbon:
    def DrawBonds(self, t : turtle.RawTurtle, numBonds : int, currentHeading : float) -> None:
        xFix = 0 # This is mostly for cyclical formulas since the angles
        yFix = 0
        if(0 <= currentHeading <= 30):
            yFix = 5
        elif(30 < currentHeading <= 60):
            xFix = 5
            yFix = 5
        else:
            xFix = 5
        
        currentPosX = t.xcor()
        currentPosY = t.ycor()
        t.forward(30) # This is for the main one
        finalPosX = t.xcor()
        finalPosY = t.ycor()
        if(numBonds == 2):
            t.penup()
            t.goto(currentPosX - xFix, currentPosY - yFix)
            t.pendown()
            t.forward(30)
        if(numBonds == 3):
            t.penup()
            t.goto(currentPosX - xFix, currentPosY - yFix)
            t.pendown()
            t.forward(30)
            t.penup()
            t.goto(currentPosX + yFix, currentPosY + yFix)
            t.pendown()
            t.forward(30)
        t.penup()
        t.goto(finalPosX, finalPosY)
        t.pendown()
    
    def DrawHydroCarbonComplex(self, t : turtle.RawTurtle, mainCarbonCount : int, compoundData : list, bondPositions : list) -> None:
        # First calculate a position to center the formula (turtle starts at coords 0,0)
        t.penup()
        t.goto(len(compoundData) * -25, t.ycor()) # Rough calculation that should do the trick for now
        
        t.write(self.CalculateHydrogens(compoundData, 0, bondPositions), font=("Arial", 14, "normal")) # This logic is incorrect
        for i in range(1, mainCarbonCount):
            t.forward(10) # This doesnt seem to draw
            t.goto(t.xcor() + 20, t.ycor() + 7)
            t.pendown()
            self.DrawBonds(t, bondPositions[i], t.heading())
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

    def CalculateHydrogens(self, compoundData : list, i : int, bondPositions : list) -> str: # This doesnt work
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

        try:
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
        except(TypeError):
            t.goto(t.xcor() + 7, t.ycor() + 20 * multiplier)
            t.pendown()
            t.forward(25)
            t.penup()
            t.goto(t.xcor() - 7, t.ycor() - 20 * multiplier)
            if(heading == 270):
                t.forward(15)
            t.forward(25)
            t.write(compoundDataElement, font=("Arial", 14, "normal"))
            t.setheading(0)
            t.goto(currentPosX, currentPosY)
            
if __name__ == "__main__":
    compoundData = [0, [1, 1], 'Br', 1, 2, 0, 0]
    bondPositions = [1, 1, 2, 1, 1, 1, 1]
