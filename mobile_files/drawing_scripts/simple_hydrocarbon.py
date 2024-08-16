from drawing_scripts.tivy import Tivy
import time

class SimpleHydrocarbon:
    def DrawHydrocarbonResidue(self, currentAngle : float, t : Tivy, compoundDataElement : int): # This needs reworking
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

    def DrawAdditionalInfo(self, compoundData : list, i : int, t : Tivy) -> None:
        currentHeading = t.heading()
        if(compoundData[i] != 0): # These parts just mean that it draws so residue part and then continues drawing the backbone
            if(type(compoundData[i]) is list):
                self.DrawHydrocarbonResidue(0, t, compoundData[i][0])
                self.DrawHydrocarbonResidue(180, t, compoundData[i][1])
            else:
                self.DrawHydrocarbonResidue(0, t, compoundData[i])
        t.setheading(currentHeading)

    def DrawHydrocarbonSimple(self, t : Tivy, mainCarbonCount : int, compoundData : list, bondPositions : list) -> None:
        t.penup()
        t.goto(250, 250) 
        t.pendown()

        t.setheading(30)
        for i in range(0, mainCarbonCount - 1): # -1 since each end point is a carbon
            if(t.heading() == 30.0):
                self.DrawAdditionalInfo(compoundData, i, t)
                self.DrawBonds(t, bondPositions[i], t.heading())
                t.setheading(330)
            else:
                self.DrawAdditionalInfo(compoundData, i, t) # Residue
                self.DrawBonds(t, bondPositions[i], t.heading()) # Bonds
                t.setheading(30)
        time.sleep(0.5)
    
    def DrawBonds(self, t : Tivy, numBonds : int, currentHeading : float) -> None:
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