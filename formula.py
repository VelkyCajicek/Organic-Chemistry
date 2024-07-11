import re

unbranchedAlkanes = ["methan", "ethan", "propan", "butan", "pentan", "hexan", "heptan", "oktan", "nonan", "dekan"]
preffixList = ["di", "tri", "tetra", "penta", "hexa"]
suffixList = ["an", "en", "yn"]

def inputFormat(inputString : str):
    bondPositions = []
    pattern = re.compile(r"\d-[A-Za-z]n")

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

    # Removes preffixes
    for i in range(0, len(returnList)):
        for preffix in preffixList: # Removes preffix
            if(preffix in returnList[i]):
                if(preffix != returnList[i]): # Because of "hexa" being in preffix and carbon list
                    returnList[i] = str(returnList[i]).replace(preffix, "")

    # Finalizes list and creates bond list
    for i in range(0, len(returnList)):
        try: # I dont like 2 try catch statements but they seem to do the trick (First one because if there are 2 types of bonds the list gets shortened too much)
            if(bool(pattern.search(returnList[i])) == True): # Checks if there is an occurence of a multiple bond
                positions = list(re.findall(r'[0-9]+', returnList[i]))
                returnList[i] = re.sub(r'[^a-zA-Z]', '', returnList[i]) 
                if(returnList[i] == "en"):
                    bondPositions.extend(positions)
                    bondPositions.append(2)
                if(returnList[i] == "yn"):
                    bondPositions.extend(positions)
                    bondPositions.append(3)
                try:
                    if(bool(pattern.search(returnList[i + 1])) == True): # Checks if there are multiple occurences of multiple bonds
                        positions = list(re.findall(r'[0-9]+', returnList[i + 1])) # Finds nums
                        returnList[i+1] = re.sub(r'[^a-zA-Z]', '', returnList[i + 1]) # Removes all special chars and nums
                        if(returnList[i+1] == "en"):
                            bondPositions.extend(positions)
                            bondPositions.append(2)
                        if(returnList[i+1] == "yn"):
                            bondPositions.extend(positions)
                            bondPositions.append(3)
                except(IndexError): #
                    pass

                returnList = list(filter(lambda a: len(a) != 2, returnList)) # Removes all strings that have the len 2, assuming only the suffix stays

                for alkane in unbranchedAlkanes:
                    if(f"{returnList[-1]}n" == alkane):
                        returnList[-1] += "n"
                        break
                    if(f"{returnList[-1]}an" == alkane):
                        returnList[-1] += "an"
                        break
        except(IndexError):
            break

    return returnList[::-1], bondPositions[::-1] # Reversed list so it starts with a int + append() > insert()

def extractValues(listElement : str, residuesList : list) -> None: # Void that changes the list
    positions = re.findall(r'[0-9]+', listElement) # Finds nums
    listElement = re.sub(r'[^a-zA-Z]', '', listElement) # Removes all special chars and nums
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
    currentBondType = 1
    bondsPositions = [1] * backboneLength
    for i in range(0, len(bondList)):
        if(type(bondList[i]) is int):
            currentBondType = bondList[i]
        else:
            bondsPositions[int(bondList[i]) - 1] = currentBondType
    return bondsPositions

def mainFormula(inputString : str):
    backboneLength = 0
    compound, bondList = inputFormat(inputString)

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
    testString = "3,4-diethyl-4-methyl-5,5-dipropyl-nona-1,6-dien"
    #testString = "4,5-dipropyl-nona-2,6-diyn"
    print(inputFormat(testString))
    #print(findMultipleBonds(inputFormat(testString)))
    print(mainFormula(testString))