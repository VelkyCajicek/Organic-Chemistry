import turtle

class AromaticHydrocarbon:
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
    
    def DrawNaphthalene(self, t : turtle.RawTurtle, compoundData : list):
        t.setheading(30)
        for i in range(0, 5):
            if(i % 2 == 0):
                self.DrawBonds(t, 2, t.heading())
                self.DrawCyclicalHydrogenAdditionalInfo(compoundData, i, t)
            else:
                self.DrawBonds(t, 1, t.heading())
                self.DrawCyclicalHydrogenAdditionalInfo(compoundData, i, t)
            t.right(60)
        t.setheading(210)
        for i in range(5, 11):
            if(i % 2 == 0):
                self.DrawBonds(t, 1, t.heading())
                try:
                    self.DrawCyclicalHydrogenAdditionalInfo(compoundData, i, t)
                except(IndexError):
                    pass
            else:
                self.DrawBonds(t, 2, t.heading())
                try:
                    self.DrawCyclicalHydrogenAdditionalInfo(compoundData, i, t)
                except(IndexError):
                    pass
            t.right(60)

    def DrawResidue(self, currentAngle : float, t : turtle.RawTurtle, compoundDataElement : int):
        currentPosX = t.xcor()
        currentPosY = t.ycor()

        t.setheading(t.heading() - currentAngle) # Very important

        t.forward(30)
        t.left(30)
        currentHeading = t.heading()
        for _ in range(0, compoundDataElement - 1):
            if(t.heading() == currentHeading):
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
        calculation = (360  - (360 / len(compoundData))) 
        if(compoundData[i] != 0): 
            if(type(compoundData[i]) is list): 
                self.DrawResidue(calculation + calculation / 3 + 180, t, compoundData[i][0])
                self.DrawResidue(calculation / 3 + 180, t, compoundData[i][1])
            else:
                self.DrawResidue(calculation / 2 + 180, t, compoundData[i]) # + 180 seems to do the trick when it comes to making sure the residue is the right way
        t.setheading(currentHeading)
