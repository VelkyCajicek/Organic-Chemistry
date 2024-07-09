import re

unbranchedAlkanes = ["methan", "ethan", "propan", "butan", "pentan", "hexan", "heptan", "oktan", "nonan", "dekan"]
preffixList = ["di", "tri", "tetra", "penta", "hexa"]
suffixList = ["an", "en", "yn"]
regexList = [r"\d-en", r"\d-yn"] # I dont like this solution so it would be good to change it

def inputFormat(inputString : str):
    bondPositions = []
    compoundFirstSplit = inputString.split("-")
    returnList = []
    iterationSkip = 100 # This is so that i can skip over an iteration if the list element has been changed
    for i in range(0, len(compoundFirstSplit)): # This goes over the string and splits everything 
        if(iterationSkip == i):
            continue
        elif(not re.search('[a-zA-Z]', compoundFirstSplit[i])):
            returnList.append("-".join(compoundFirstSplit[i:i+2]))
            iterationSkip = i + 1
        else:
            returnList.append(compoundFirstSplit[i])
 
    for i in range(0, len(returnList)): # This checks for the num of bonds
        for preffix in preffixList: # Removes preffix
            if(preffix in returnList[i]):
                returnList[i] = returnList[i].replace(preffix, "")
                if(i == len(returnList) - 1): # If there is a preffix then remove the last char from previous element
                    returnList[i-1] = returnList[i-1][:-1] 

        for index in range(0, len(regexList)):
            patternCheck = re.compile(regexList[index])
            if(bool(patternCheck.search(returnList[i])) == True):
                bondPositions = re.findall(r'[0-9]+', returnList[i]) # Finds nums
                if(index == 0):
                    bondPositions.insert(0, 2)
                else:
                    bondPositions.insert(0, 3)
                returnList[i] = re.sub(r'[^a-zA-Z]', '', returnList[i])
                # Adds an to the end of the string
                for part in returnList:
                    for suffix in suffixList:
                        if(suffix == part):
                            part = suffixList[0]
                            returnList[i-1] += part 
    
    returnList = list(filter(lambda a: len(a) != 2, returnList)) # Removes all strings that have the len 2, assuming only the suffix stays
    return returnList, bondPositions

def extractValues(listElement : str, residuesList : list) -> None: # Void that changes the list
    positions = re.findall(r'[0-9]+', listElement) # Finds nums
    listElement = re.sub(r'[^a-zA-Z]', '', listElement) # Removes all special chars and nums
    for preffix in preffixList:
        listElement = listElement.replace(preffix, "")
    for i in range(0, len(unbranchedAlkanes)): # Goes through pre-defined list
        if(unbranchedAlkanes[i].replace("an", "yl") == listElement): # Checks if listElement is in this predefined list
            for index in positions: 
                if(residuesList[int(index) - 1] == i + 1): # This indexing works and at the time of writing this code i dont want to re-check it
                    residuesList[int(index) - 1] = [residuesList[int(index) - 1]] # Converts list variable into a list 
                    residuesList[int(index) - 1].append(i + 1)
                elif(type(residuesList[int(index) - 1]) is list): # If there is already a list there it just adds another element of that type
                    residuesList[int(index) - 1].append(i + 1)
                else:
                    residuesList[int(index) - 1] = i + 1 # Regex returns nums as strings

def bondFormat(bondList : list, backboneLength : int) -> list:
    bondsPositions = [0] * backboneLength
    for i in range(1, len(bondList)):
        bondsPositions[int(bondList[i]) - 1] = int(bondList[0])
    return bondsPositions

def mainFormula(inputString : str):
    backboneLength = 0
    compound, bondList = inputFormat(inputString)
    compound = compound[::-1] # Reverse the list because its done the opposite way
    for i in range(0, len(unbranchedAlkanes)): # First find the number of carbon on the backbone
        if(compound[0] == unbranchedAlkanes[i]):
            backboneLength = i + 1
            break

    hydrocarbonResidues = [0] * backboneLength
    bondPositions = bondFormat(bondList, backboneLength)

    compound.pop(0) # Removes the part of the compound that determines the backbone length
    for element in compound:
        extractValues(element, hydrocarbonResidues)

    return hydrocarbonResidues, bondPositions

if __name__ == "__main__":
    testString = "2,3,3,7-tetrameth-2-yl-okt-1,2-en"
    testString = "4-propyl-deka-2,4-dien" 
    #testString = "4-ethyl-3,5-dimethyl-oktan"
    #print(inputFormat(testString))
    #print(findMultipleBonds(inputFormat(testString)))
    print(mainFormula(testString))