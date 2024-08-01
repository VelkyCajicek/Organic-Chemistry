import math

class Tivy():
    def __init__(self) -> None:
        self.currentHeading = 0
        self.currentPosition = [0,0]
        
    def foward(self, distance : float) -> None:
        xAxisCalculation = math.sin(math.radians(90 - self.currentHeading)) / math.sin(math.radians(90)) * distance
        yAxisCalculation = math.sin(math.radians(self.currentHeading)) / math.sin(math.radians(90)) * distance
        self.currentPosition[0] += round(xAxisCalculation, 1)
        self.currentPosition[1] += round(yAxisCalculation, 2)

    def setheading(self, heading : float) -> None:
        self.currentHeading = heading
        
    def heading(self) -> float:
        return self.currentHeading
    
    def setpos(self, xCoord : float, yCoord : float) -> None:
        self.currentPosition = [xCoord, yCoord]
    
if __name__ == "__main__":
    t = Tivy()
    t.foward(30)
    print(t.currentPosition)
    t.setheading(30)
    t.foward(30)
    print(t.currentPosition)
    print(t.heading())
    
    