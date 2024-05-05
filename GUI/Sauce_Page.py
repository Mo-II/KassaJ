import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib as mpl
import numpy as np


class SaucePage():

    def setDefaultValue(self, list):
        dict = {}
        for sauce in list:
            dict[sauce] = 0
            print(dict)
        return dict


    def __init__(self, master, event_name, event_id, db, parent, saucesList, flag = False, amountList= None):
        if amountList is None:
            amountList = self.setDefaultValue(saucesList)
        self.master = master
        self.event_name = event_name
        self.amountList = amountList
        self.last_event_id = event_id
        self.db = db
        self.flag = flag
        self.parent = parent


        master.attributes('-fullscreen', True)

              
        print(amountList)

    def open(self):
        self.master.title(str(self.event_name))
        label = tk.Label(self.master, text="Sauces")
        label.grid(row=0,column=0)
        label = tk.Label(self.master, text="Amount")
        label.grid(row=0,column=1)

        index = 0
        for sauce,amount in self.amountList.items():
            sauceAmountLabel = tk.Label(self.master, text=self.amountList[sauce],font=("Arial",20))
            sauceAmountLabel.grid(row=index+1,column=2,padx=50, pady=10)
            button = tk.Button(self.master, text=sauce, command=lambda label=sauceAmountLabel, s=sauce: self.addToAmount(label, s, self.amountList),font=("Arial",20))
            button.grid(row=index+1,column=0,padx=50, pady=10)
            buttonmin = tk.Button(self.master, text='-', command=lambda label=sauceAmountLabel, s=sauce: self.subtractFromAmount(label, s,self.amountList),font=("Arial",20))
            buttonmin.grid(row=index+1,column=1,padx=50, pady=10)
            index += 1
        

        if not self.flag: 
            submit = tk.Button(self.master, text='Submit', command=lambda s=self.amountList: self.submitSauces(s),font=("Arial",20)) #Sauzen schrijven naar excel file
        else:    
            submit = tk.Button(self.master, text='Submit', command=lambda s=self.amountList: self.replaceSauces(s),font=("Arial",20)) #Sauzen schrijven naar excel file
        submit.grid(row=index+1,column=0,padx=50, pady=10)
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=0,column=3,rowspan=10)
        self.toolbar = NavigationToolbar2Tk(self.canvas,self.master, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(row=11,column=3, sticky="nsew")
        self.draw_plot()
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)
            

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

    #(self, event_id, event_name, sauces):
    def submitSauces(self, dict):
        self.db.write_Event(str(int(self.last_event_id) + 1), self.event_name, dict)
        self.parent.updateEvents()
        self.parent.updateComboBox()
        self.on_close()

    #(self, event_id, event_name, sauces):
    def replaceSauces(self, dict):
        self.db.replace_Event(str(int(self.last_event_id)), self.event_name, dict)
        self.parent.load_in_event()
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
        self.master.destroy()
