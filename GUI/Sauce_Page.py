import tkinter as tk

from Classes.Sauce import Sauce
from Classes.Sauces import Sauces
from Classes.CsvInterface import CsvInterface


class SaucePage:


    def __init__(self, master, sauces):
        self.master = master
        self.sauces = sauces

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
        amountList = {
            str(bolognese) : 0,
            str(carbonnara) : 0,
            str(porcini) : 0,
            str(arrabiata) : 0,
            str(tomaat) : 0,
            str(tomatensaus_met_groentjes) : 0
        }

        index = 0
        for sauce,amount in amountList.items():
            sauceAmountLabel = tk.Label(new_window, text=amountList[sauce])
            sauceAmountLabel.grid(row=index+1,column=2,padx=5, pady=5)
            button = tk.Button(new_window, text=sauce, command=lambda label=sauceAmountLabel, s=sauce: self.addToAmount(label, s, amountList))
            button.grid(row=index+1,column=0,padx=5, pady=5)
            buttonmin = tk.Button(new_window, text='-', command=lambda s=sauceAmountLabel: self.subtractFromAmount(s, sauce,amountList))
            buttonmin.grid(row=index+1,column=1,padx=5, pady=5)
            index += 1
        

        submit = tk.Button(new_window, text='Submit', command=lambda s=amountList: self.submitSauces(s, new_window))
        submit.grid(row=index+1,column=0,padx=5, pady=5)
            

    def addToAmount(self, label, sauce, amountList):
        amountList[sauce] += 1
        label.config(text=amountList[sauce])
        print(amountList[sauce])

    def subtractFromAmount(self, label, sauce, amountList):
        amountList[sauce] -= 1
        label.config(text=amountList[sauce])
        print(amountList)

    def submitSauces(self, dict, window):
        csv = CsvInterface
        self.sauces.addDicts(dict)
        window.destroy()
