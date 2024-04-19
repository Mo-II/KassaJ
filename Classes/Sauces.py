from Classes.Sauce import Sauce

class Sauces:

    def __init__(self, sauceList) -> None:
        self.sauceList = []

    def addSauce(self, name):
        self.sauceList.append(Sauce(name))

    def addMultipleSauces(self, list):
        for sauce in list:
            self.addSauce(sauce)

    def listSauces(self):
        for sauce in self.sauceList:
            print(sauce)

