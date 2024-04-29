import tkinter as tk
from GUI.Sauce_Page import SaucePage
from Classes.Sauces import Sauces
from Classes.CsvInterface import CsvInterface
from tkinter import font as tkfont
from tkinter import ttk
import csv


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

    