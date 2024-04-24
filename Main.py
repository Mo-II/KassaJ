from Classes.Sauce import Sauce
from Classes.Sauces import Sauces
from GUI.LandingPage import LandingPage # type: ignore
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

    #for sauce in sauces.sauceList:
    #    button = tk.Button(root, text=sauce.name, command=lambda s=sauce: print(s.name))
    #    button.pack()
    
    root.mainloop()


if __name__ == '__main__':
    main()