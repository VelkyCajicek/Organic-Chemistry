import time
import turtle

class CyclicalHydrocarbon:
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
    
    def DrawCyclicalHydrogen(self, t : turtle.RawTurtle, mainCarbonCount : int, compoundData : list, bondPositions : list):
        for i in range(0, mainCarbonCount):
            self.DrawCyclicalHydrogenAdditionalInfo(compoundData, i, t)
            self.DrawBonds(t, bondPositions[i], t.heading())
            t.left(360 / mainCarbonCount)
        time.sleep(0.5)

    def DrawHydrocarbonResidueCyclical(self, currentAngle : float, t : turtle.RawTurtle, compoundDataElement : int): # This needs reworking
        currentPosX = t.xcor()
        currentPosY = t.ycor()

        t.setheading(t.heading() - currentAngle) # Very important

        t.forward(30)
        t.left(30)
        currentHeading = t.heading()
        try:
            for _ in range(0, compoundDataElement - 1):
                if(t.heading() == currentHeading):
                    t.forward(30)
                    t.right(60) 
                else:
                    t.forward(30)
                    t.left(60)
        except(TypeError):
            t.penup()
            if(t.heading() == currentHeading):
                t.forward(30)
                t.right(60) 
            else:
                t.forward(30)
                t.left(60)
            t.write(compoundDataElement, font=("Arial", 14, "normal"))
        t.penup()
        t.goto(currentPosX, currentPosY) # Resets position
        t.pendown()

    def DrawCyclicalHydrogenAdditionalInfo(self, compoundData : list, i : int, t : turtle.RawTurtle):
        currentHeading = t.heading()
        calculation = (360  - (360 / len(compoundData))) # Im retarded, I hate myself, it was this all along
        if(compoundData[i] != 0): # These parts just mean that it draws so residue part and then continues drawing the backbone
            if(type(compoundData[i]) is list): 
                self.DrawHydrocarbonResidueCyclical(calculation + calculation / 3, t, compoundData[i][0])
                self.DrawHydrocarbonResidueCyclical(calculation / 3, t, compoundData[i][1])
            else:
                self.DrawHydrocarbonResidueCyclical(calculation / 2, t, compoundData[i])
        t.setheading(currentHeading)