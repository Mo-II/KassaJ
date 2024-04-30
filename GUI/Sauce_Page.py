import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib as mpl
import numpy as np

from Classes.Sauce import Sauce
from Classes.Sauces import Sauces
from Classes.CsvInterface import CsvInterface


class SaucePage:


    def __init__(self, master, sauces):
        self.master = master
        self.sauces = sauces
        bolognese = Sauce("Bolognese met vlees van BUTCHER's De Laet")
        carbonnara = Sauce("Carbonara")
        porcini = Sauce("Porcini")
        arrabiata = Sauce("Arrabiata")
        tomaat = Sauce("Tomaat Mascarpone")
        tomatensaus_met_groentjes = Sauce("Tomatensaus Met Groentjes")

        self.amountList = {
            str(bolognese) : 0,
            str(carbonnara) : 0,
            str(porcini) : 0,
            str(arrabiata) : 0,
            str(tomaat) : 0,
            str(tomatensaus_met_groentjes) : 0
        }

    def open(self):
        self.new_window = tk.Toplevel(self.master)
        self.new_window.title("Sauce window")
        label = tk.Label(self.new_window, text="Sauces")
        label.grid(row=0,column=0)
        label = tk.Label(self.new_window, text="Amount")
        label.grid(row=0,column=1)

        index = 0
        for sauce,amount in self.amountList.items():
            sauceAmountLabel = tk.Label(self.new_window, text=self.amountList[sauce])
            sauceAmountLabel.grid(row=index+1,column=2,padx=5, pady=5)
            button = tk.Button(self.new_window, text=sauce, command=lambda label=sauceAmountLabel, s=sauce: self.addToAmount(label, s, self.amountList))
            button.grid(row=index+1,column=0,padx=5, pady=5)
            buttonmin = tk.Button(self.new_window, text='-', command=lambda label=sauceAmountLabel, s=sauce: self.subtractFromAmount(label, s,self.amountList))
            buttonmin.grid(row=index+1,column=1,padx=5, pady=5)
            index += 1
        

        submit = tk.Button(self.new_window, text='Submit', command=lambda s=self.amountList: self.submitSauces(s))
        submit.grid(row=index+1,column=0,padx=5, pady=5)
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.new_window)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=0,column=3,rowspan=10)
        self.toolbar = NavigationToolbar2Tk(self.canvas,self.new_window, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(row=11,column=3, sticky="nsew")
        self.draw_plot()
        self.new_window.protocol("WM_DELETE_WINDOW", self.on_close)
            

    def addToAmount(self, label, sauce, amountList):
        amountList[sauce] += 1
        label.config(text=amountList[sauce])
        self.draw_plot()
        print(amountList[sauce])

    def subtractFromAmount(self, label, sauce, amountList):
        amountList[sauce] -= 1
        label.config(text=amountList[sauce])
        self.draw_plot()
        print(amountList)

    def submitSauces(self, dict):
        csv = CsvInterface
        self.sauces.addDicts(dict)
        self.on_close()
        

    def draw_plot(self):
        self.ax.clear()
        sauces = []
        amounts = []
        cmap = mpl.colormaps['rainbow']
        for sauce,amount in self.amountList.items():
            sauces.append(sauce)
            amounts.append(amount)
        colors = cmap(np.linspace(0, 1, len(sauces)))
        bars = self.ax.bar(sauces, amounts, color=colors)
        plt.gca().set_xticks([])
        self.ax.legend(bars,sauces,loc='center left', bbox_to_anchor=(1, 0.5),fontsize='small')
        self.fig.tight_layout()
        self.canvas.draw()

    def on_close(self):
        plt.close(self.fig)
        self.new_window.destroy()
