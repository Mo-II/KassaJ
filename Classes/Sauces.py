from Classes.Sauce import Sauce

class Sauces:
    

    def __init__(self) -> None:
        self.sauceList = ["Bolognese met vlees van BUTCHER's De Laet","Carbonara","Porcini","Arrabiata" ]
        self.saucesDict = {"Bolognese met vlees van BUTCHER's De Laet":0,"Carbonara":0,"Porcini":0,"Arrabiata":0,"Tomaat Mascarpone":0,"Tomatensaus Met Groentjes":0}

    def addSauce(self, name):
        self.sauceList.append(Sauce(name))

    def addDicts(self, dict):
        self.saucesDict = dict
        print(self.saucesDict)

    def emptyDict(self):
        self.saucesDict = {"Bolognese met vlees van BUTCHER's De Laet":0,"Carbonara":0,"Porcini":0,"Arrabiata":0,"Tomaat Mascarpone":0,"Tomatensaus Met Groentjes":0}