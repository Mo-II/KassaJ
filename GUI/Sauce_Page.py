import tkinter as tk

from Classes.Sauce import Sauce
from Classes.Sauces import Sauces
from Classes.CsvInterface import CsvInterface


class SaucePage:
    def __init__(self, master):
        self.master = master

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

        sauces = Sauces([])
        sauces.addMultipleSauces([bolognese, carbonnara, porcini, arrabiata, tomaat, tomatensaus_met_groentjes])
        sauces.listSauces()
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

    def submitSauces(self, list, window):
        csv = CsvInterface
        csv.writeSauces(csv, 1, list) #1 Is de Event ID, dit zou automatisch moeten aangemaakt worden, een unieke Event ID, die gaat worden gebruikt in CsvInterface om te writen
        window.destroy()
