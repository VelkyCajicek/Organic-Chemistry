# https://www.skola-chrast.net/userFiles/tridy1920/9a/nazvoslovi-organicke-chemie-kompletni-text-.pdf Link to nomenculture

class HydrocarbonDerivative:
    def __init__(self, name : str, functionalGroup : str, preffix : str, suffix : str) -> None:
        self.name = name
        self.functionalGroup = functionalGroup
        self.preffix = preffix
        self.suffix = suffix

class AromaticCompound:
    def __init__(self, name : str, formula : str) -> None:
        self.name = name
        self.formula = formula

HydrocarbonDerivativeList = [
    HydrocarbonDerivative("Fluorderivát", "F", "fluor", "-----"),
    HydrocarbonDerivative("Chlorderivát", "Cl", "chlor", "-----"),
    HydrocarbonDerivative("Bromderivát", "Br", "brom", "-----"),
    HydrocarbonDerivative("Jodderivát", "I", "jod", "-----"),
    HydrocarbonDerivative("Nitrosoderivát", "NO", "nitroso", "-----"),
    HydrocarbonDerivative("Nitroderivát", "NO2", "nitro", "-----"),
    HydrocarbonDerivative("Amin", "NH2", "-----", "amin"),
    HydrocarbonDerivative("Alkohol", "OH", "-----", "ol"),
    HydrocarbonDerivative("Fenol", "OH", "-----", "ol"),
    HydrocarbonDerivative("Ether", "OR", "alkoxy nebo aroxy", "-----"),
    HydrocarbonDerivative("Aldehyd", "CHO", "-----", "al"),
    HydrocarbonDerivative("Keton", "COR", "-----", "on"),
    HydrocarbonDerivative("Karboxylová kyselina", "COOH", "-----", "ová kyselina"),
    HydrocarbonDerivative("Ester", "COOR", "-----", "oát") 
]

AromaticCompounds = [
    AromaticCompound("benzen", "cyklohexa-1,3,5-trien"),
    AromaticCompound("toluen", "1-methyl-cyklohexa-1,3,5-trien"),
    AromaticCompound("o-dimethylbenzen", "1,2-dimethyl-benzen"),
    AromaticCompound("m-dimethylbenzen", "1,3-dimethyl-benzen"),
    AromaticCompound("p-dimethylbenzen", "1,4-dimethyl-benzen")
]