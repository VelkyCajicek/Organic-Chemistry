import re

class FormulaConversion:
    def __init__(self) -> None:
        self.unbranchedAlkanes = ["methan", "ethan", "propan", "butan", "pentan", "hexan", "heptan", "oktan", "nonan", "dekan"]
        self.preffixList = ["di", "tri", "tetra", "penta", "hexa"]

    def inputFormat(self, inputString : str) -> list:
        compoundFirstSplit = inputString.split("-") 
        returnList = []
        iterationSkip = 100 # This is so that i can skip over an iteration if the list element has been changed

        for i in range(0, len(compoundFirstSplit)):
            if(iterationSkip == i):
                continue
            elif(not re.search('[a-zA-Z]', compoundFirstSplit[i])):
                returnList.append("-".join(compoundFirstSplit[i:i+2]))
                iterationSkip = i + 1
            else:
                returnList.append(compoundFirstSplit[i])

        return returnList

    def extractValues(self, listElement : str, residuesList : list) -> None: # Void that changes the list
        positions = re.findall(r'[0-9]+', listElement) # Finds nums
        listElement = re.sub(r'[^a-zA-Z]', '', listElement) # Removes all special chars and nums
        for preffix in self.preffixList:
            listElement = listElement.replace(preffix, "")

        for i in range(0, len(self.unbranchedAlkanes)): # Goes through pre-defined list
            if(self.unbranchedAlkanes[i].replace("an", "yl") == listElement): # Checks if listElement is in this predefined list
                for index in positions: 
                    if(residuesList[int(index) - 1] == i + 1): # This indexing works and at the time of writing this code i dont want to re-check it
                        residuesList[int(index) - 1] = [residuesList[int(index) - 1]] # Converts list variable into a list 
                        residuesList[int(index) - 1].append(i + 1)
                    elif(type(residuesList[int(index) - 1]) is list): # If there is already a list there it just adds another element of that type
                        residuesList[int(index) - 1].append(i + 1)
                    else:
                        residuesList[int(index) - 1] = i + 1 # Regex returns nums as strings

    def mainFormula(self, inputString : str):
        backboneLength = 0

        compound = self.inputFormat(inputString)[::-1] # Reverse the list because its done the opposite way

        for i in range(0, len(self.unbranchedAlkanes)): # First find the number of carbon on the backbone
            if(compound[0] == self.unbranchedAlkanes[i]):
                backboneLength = i + 1
                break
            
        hydrocarbonResidues = [0] * backboneLength
        compound.pop(0) # Removes the part of the compound that determines the backbone length

        for element in compound:
            self.extractValues(element, hydrocarbonResidues)

        return hydrocarbonResidues

if __name__ == "__main__":
    #testString = "4-ethyl-3,5-dimethyl-oktan"
    testString = "7-ethyl-2,2,6-trimethyl-5-propyl-dekan"
    testString = "2,3,7-trimethyl-nonan"
    conversion = FormulaConversion()
    print(conversion.mainFormula(testString))