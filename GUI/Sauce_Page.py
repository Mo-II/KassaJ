import tkinter as tk

from Classes.Sauce import Sauce
from Classes.Sauces import Sauces

class SaucePage:
    def __init__(self, master):
        self.master = master
        self.amountList = [0,0,0,0,0,0]

    def open(self):
        new_window = tk.Toplevel(self.master)
        new_window.title("Sauce window")
        label = tk.Label(new_window, text="Sauces")
        label.grid(row=0,column=0)
        label = tk.Label(new_window, text="Amount")
        label.grid(row=0,column=1)
        bolognese = Sauce("Bolognese met vlees van BUTCHER's De Laet")
        carbonnara = Sauce('Carbonara')
        porcini = Sauce('Porcini')
        arrabiata = Sauce('Arrabiata')
        tomaat = Sauce('Tomaat Mascarpone')
        tomatensaus_met_groentjes = Sauce('Tomatensaus Met Groentjes')
        self.amountList = [0,0,0,0,0,0]

        sauces = Sauces([])
        sauces.addMultipleSauces([bolognese, carbonnara, porcini, arrabiata, tomaat, tomatensaus_met_groentjes])
        sauces.listSauces()
        for index,sauce in enumerate(sauces.sauceList):
            sauceAmountLabel = tk.Label(new_window, text=self.amountList[index])
            sauceAmountLabel.grid(row=index+1,column=2,padx=5, pady=5)
            button = tk.Button(new_window, text=sauce.name, command=lambda i=index, s=sauceAmountLabel: self.addToAmount(i,s))
            button.grid(row=index+1,column=0,padx=5, pady=5)
            buttonmin = tk.Button(new_window, text='-', command=lambda i=index,s=sauceAmountLabel: self.subtractFromAmount(i,s))
            buttonmin.grid(row=index+1,column=1,padx=5, pady=5)
            

    def addToAmount(self,position,label):
        self.amountList[position] = self.amountList[position] + 1
        label.config(text=self.amountList[position])
        print(self.amountList[position])

    def subtractFromAmount(self,position,label):
        self.amountList[position] = self.amountList[position] - 1
        label.config(text=self.amountList[position])
        print(self.amountList)