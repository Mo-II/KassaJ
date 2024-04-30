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
import json
import matplotlib as mpl


class LandingPage:
    def __init__(self, master, currEvent):
        self.sauces = Sauces([])
        self.master = master
        self.event = currEvent
        self.last_event_id = 0
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

        self.close_button = tk.Button(master, text="Close", command=self.on_close, height=2, width=10, font=large_font)
        self.close_button.pack(side=tk.BOTTOM, anchor='w', padx=10, pady=10)

        self.events = self.read_events_from_csv('Sauzen.csv')

        # Create a combobox to list events
        self.event_combobox = ttk.Combobox(master, values=self.events)
        self.event_combobox.pack(pady=20, padx=20, anchor='nw')
        self.event_combobox.bind("<<ComboboxSelected>>", self.load_in_event)

        #buttons voor grafiek aan te passen
        self.buttonEvent = tk.Button(master, text="event", command=self.plot_event)
        self.buttonEvent.pack(pady=20, padx=20, anchor='nw',side='left')
        self.buttonWeek = tk.Button(master, text="week", command=self.plot_week)
        self.buttonWeek.pack(pady=20, padx=20, anchor='nw',side='left')
        self.buttonMonth = tk.Button(master, text="month", command=self.plot_month)
        self.buttonMonth.pack(pady=20, padx=20, anchor='nw')
        #code voor grafiek
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(pady=20, padx=20, anchor='nw')
        self.toolbar = NavigationToolbar2Tk(self.canvas,self.master, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.pack(pady=20, padx=20, anchor='nw')
        self.plot_event() # moet de gene worden voor events want die gaan we standaard showen

    def endEvent(self, dict):
        csvInterface = CsvInterface()  
        csvInterface.writeSauces(str(self.last_event_id+1),self.event, dict)
        print(dict, 'written!')

    
    def read_events_from_csv(self, filepath):
        """Read events from a CSV file and return them as a list."""
        events = []
        try:
            with open(filepath, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    events.append(row[1])  # Assuming event names are in the first column
                self.last_event_id = int(row[0])
        except FileNotFoundError:
            print("The file was not found.")
        except Exception as e:
            print("An error occurred:", e)
        return events
        

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

    def search_event(self, filepath, event_id, event):
        """Read events from a CSV file and return them as a list."""
        sauces = []
        amounts = []
        try:
            with open(filepath, newline='', encoding='utf-8') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    if row[1] == event and row[0] == str(event_id):
                        print("nnnn")
                        data_dict = json.loads(row[3])
                        for key, value in data_dict.items():
                            sauces.append(key)
                            amounts.append(value)
                        return sauces,amounts
        except FileNotFoundError:
            print("The file was not found.")
        except Exception as e:
            print("An error occurred:", e)
        return sauces,amounts

    def load_in_event(self,event):
        self.ax.clear()
        sauces, amounts = self.search_event('Sauzen.csv',self.event_combobox.current()-1, self.event_combobox.get())
        cmap = mpl.colormaps['rainbow']
        colors = cmap(np.linspace(0, 1, len(sauces)))
        bars = self.ax.bar(sauces, amounts, color=colors)
        plt.gca().set_xticks([])
        self.ax.legend(bars,sauces,loc='center left', bbox_to_anchor=(1, 0.5),fontsize='small')
        self.fig.tight_layout()
        self.canvas.draw()

    def on_close(self):
        plt.close(self.fig)
        self.master.destroy()

    
        

    