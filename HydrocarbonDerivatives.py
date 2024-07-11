class HydrocarbonDerivative:
    def __init__(self, name : str, functionalGroup : str, preffix : str, suffix : str) -> None:
        self.name = name
        self.functionalGroup = functionalGroup
        self.preffix = preffix
        self.suffix = suffix

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