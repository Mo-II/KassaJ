import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from GUI.Sauce_Page import SaucePage
import numpy as np


class LandingPage:
    def __init__(self, master):
        self.master = master
        master.title("Simple GUI")
        SaucesPage = SaucePage(master)
        #buttons voor grafiek aan te passen
        self.buttonEvent = tk.Button(master, text="event", command=self.plot_event())
        self.buttonEvent.grid(row=0,column=0)
        self.buttonWeek = tk.Button(master, text="week", command=self.plot_week())
        self.buttonWeek.grid(row=0,column=1)
        self.buttonMonth = tk.Button(master, text="month", command=self.plot_month())
        self.buttonMonth.grid(row=0,column=2)
        self.button = tk.Button(master, text="New event", command=SaucesPage.open)
        self.button.grid(row=5,column=10)
        #code voor grafiek
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.grid(row=1,column=0,columnspan=3, sticky="nsew")
        self.toolbar = NavigationToolbar2Tk(self.canvas,self.master, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.grid(row=2,column=0,columnspan=3, sticky="nsew")
        self.plot_event() # moet de gene worden voor events want die gaan we standaard showen
        self.master.protocol("WM_DELETE_WINDOW", self.on_close)
        

    def say_hello(self):
        print("Hello, button clicked!")

    def plot_event(self):
            self.ax.clear()
            x = np.random.randint(0,10,10)
            y = np.random.randint(0,10,10)
            self.ax.plot(x, y)
            self.canvas.draw()
    
    def plot_week(self):
            self.ax.clear()
            x = np.random.randint(0,10,10)
            y = np.random.randint(0,10,10)
            self.ax.plot(x, y)
            self.canvas.draw()

    def plot_month(self):
            self.ax.clear()
            x = np.random.randint(0,10,10)
            y = np.random.randint(0,10,10)
            self.ax.plot(x, y)
            self.canvas.draw()

    def on_close(self):
        plt.close(self.fig)
        self.master.destroy()

    
        

    