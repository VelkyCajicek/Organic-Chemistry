import math

from kivy.graphics import *

class Tivy():
    def __init__(self) -> None:
        self.currentHeading = 0
        self.currentPosition = [0,0]
        self.penActive = True
        
    def forward(self, distance : float) -> None:
        startPos = self.currentPosition.copy()
        xAxisCalculation = math.sin(math.radians(90 - self.currentHeading)) / math.sin(math.radians(90)) * distance
        yAxisCalculation = math.sin(math.radians(self.currentHeading)) / math.sin(math.radians(90)) * distance
        self.currentPosition[0] += round(xAxisCalculation, 1)
        self.currentPosition[1] += round(yAxisCalculation, 2)
        if(self.penActive):
            Line(points=startPos + self.currentPosition)

    def xcor(self):
        return self.currentPosition[0]

    def ycor(self):
        return self.currentPosition[1]

    def penup(self):
        self.penActive = False

    def pendown(self):
        self.penActive = True

    def setheading(self, heading : float) -> None:
        self.currentHeading = heading
        
    def heading(self) -> float:
        return self.currentHeading
    
    def goto(self, xCoord : float, yCoord : float) -> None:
        self.currentPosition = [xCoord, yCoord]
    
    def left(self, angle : float) -> None:
        self.currentHeading + angle
    
    def right(self, angle : float) -> None:
        self.currentHeading - angle

if __name__ == "__main__":
    t = Tivy()
    t.forward(30)
    print(t.currentPosition)
    t.setheading(30)
    t.forward(30)
    print(t.currentPosition)
    print(t.heading())
    
    