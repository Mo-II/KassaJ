from Classes.Sauce import Sauce

class Sauces:
    saucesDict = {"Bolognese met vlees van BUTCHER's De Laet": 0, 'Carbonara' : 0, 'Porcini' : 0, 'Arrabiata': 0, 'Tomaat Mascarpone': 0, 'Tomatensaus Met Groentjes': 0}

    def __init__(self, sauceList) -> None:
        self.sauceList = []

    def addSauce(self, name):
        self.sauceList.append(Sauce(name))

    def addMultipleSauces(self, list):
        for sauce in list:
            self.addSauce(sauce)

    def addDicts(self, dict):
        for key in dict:
            self.saucesDict[key] += dict[key]
        print(self.saucesDict)

    def listSauces(self):
        for sauce in self.sauceList:
            print(sauce)