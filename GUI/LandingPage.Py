import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from GUI.Sauce_Page import SaucePage
from Classes.Sauces import Sauces
from Classes.CsvInterface import CsvInterface
from tkinter import font as tkfont
from tkinter import ttk
import csv
import numpy as np


class LandingPage:
    def __init__(self, master, currEvent):
        self.sauces = Sauces([])
        self.master = master
        self.event = currEvent
        master.title("Simple GUI")
        master.attributes('-fullscreen', True)
        large_font = tkfont.Font(family="Helvetica", size=14, weight="bold")


        SaucesPage = SaucePage(master, self.sauces)
        self.label = tk.Label(master, text="Hello, GUI!")
        self.label.pack()

        self.button = tk.Button(master, text="Sauce window!", command=SaucesPage.open, height=3, width=20, font=large_font)
        self.end = tk.Button(master, text='End Event!', command=lambda s=self.sauces.saucesDict: self.endEvent(s), height=3, width=20, font=large_font)
        self.button.pack()
        self.end.pack()
        self.button.pack(pady=10)  # Add some padding to space out the buttons
        self.end.pack(pady=10)

        self.close_button = tk.Button(master, text="Close", command=master.destroy, height=2, width=10, font=large_font)
        self.close_button.pack(side=tk.BOTTOM, anchor='w', padx=10, pady=10)

        self.events = self.read_events_from_csv('Sauzen.csv')

        # Create a combobox to list events
        self.event_combobox = ttk.Combobox(master, values=self.events)
        self.event_combobox.pack(pady=20, padx=20, anchor='nw') 

    def endEvent(self, dict):
        csvInterface = CsvInterface()  
        csvInterface.writeSauces(self.event, dict)
        print(dict, 'written!')

    
    def read_events_from_csv(self, filepath):
        """Read events from a CSV file and return them as a list."""
        events = []
        try:
            with open(filepath, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    events.append(row[0])  # Assuming event names are in the first column
        except FileNotFoundError:
            print("The file was not found.")
        except Exception as e:
            print("An error occurred:", e)
        return events
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

    
        

    