from Classes.Sauce import Sauce
from Classes.Sauces import Sauces
from GUI import LandingPage
import tkinter as tk

def main():
    bolognese = Sauce("Bolognese met vlees van BUTCHER's De Laet")
    carbonnara = Sauce('Carbonara')
    porcini = Sauce('Porcini')
    arrabiata = Sauce('Arrabiata')
    tomaat = Sauce('Tomaat Mascarpone')
    tomatensaus_met_groentjes = Sauce('Tomatensaus Met Groentjes')

    sauces = Sauces([])
    sauces.addMultipleSauces([bolognese, carbonnara, porcini, arrabiata, tomaat, tomatensaus_met_groentjes])
    sauces.listSauces()

    root = tk.Tk()
    gui = LandingPage(root)
    root.mainloop()





    

if __name__ == '__main__':
    main()