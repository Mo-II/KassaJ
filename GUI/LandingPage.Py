import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from GUI.Sauce_Page import SaucePage
from tkinter import font as tkfont
from tkinter import ttk
from tkinter import font
import numpy as np
import json
import matplotlib as mpl
from Classes.DBInterface import DBInterface


class LandingPage:
    def __init__(self, master):
        self.db = DBInterface()
        self.sauces = self.db.extract_sauces()
        self.master = master
        self.event = ''
        master.title("Simple GUI")
        master.attributes('-fullscreen', True)
        large_font = tkfont.Font(family="Helvetica", size=14, weight="bold")

        self.label = tk.Label(master, text="Landing Page")
        self.label.pack()

        self.button = tk.Button(master, text="Start Event!", command=lambda :self.open_event_window(), height=3, width=20, font=large_font) #Moet init event openen
        self.end = tk.Button(master, text='Choose Event!', command=lambda : self.chooseEvent(), height=3, width=20, font=large_font)
        self.addSauce = tk.Button(master, text='Add Sauce!', height=2, width=10, font=large_font, bg="green", command=lambda : self.add_sauce_window())
        self.button.pack()
        self.end.pack()
        self.button.pack(pady=10)  # Add some padding to space out the buttons
        self.end.pack(pady=10)

        self.close_button = tk.Button(master, text="Close", command=self.on_close, height=2, width=10, font=large_font, bg="red")
        self.close_button.pack(side=tk.BOTTOM, anchor='sw', padx=10, pady=10)
        self.addSauce.pack(side=tk.BOTTOM, anchor='se', padx=10, pady=10)

        self.updateEvents()

        # Create a combobox to list events
        self.event_combobox = ttk.Combobox(master, values=self.events)
        self.event_combobox.pack(pady=20, padx=20, anchor='nw')
        self.event_combobox.bind("<<ComboboxSelected>>", self.load_in_event)



        #buttons voor grafiek aan te passen
        # self.buttonEvent = tk.Button(master, text="event", command=self.plot_event)
        # self.buttonEvent.pack(pady=20, padx=20, anchor='nw',side='left')
        # self.buttonWeek = tk.Button(master, text="week", command=self.plot_week)
        # self.buttonWeek.pack(pady=20, padx=20, anchor='nw',side='left')
        # self.buttonMonth = tk.Button(master, text="month", command=self.plot_month)
        # self.buttonMonth.pack(pady=20, padx=20, anchor='nw')
        #code voor grafiek
        self.fig, self.ax = plt.subplots()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas_widget = self.canvas.get_tk_widget()
        self.canvas_widget.pack(pady=20, padx=20, anchor='nw')
        self.toolbar = NavigationToolbar2Tk(self.canvas,self.master, pack_toolbar=False)
        self.toolbar.update()
        self.toolbar.pack(pady=20, padx=20, anchor='nw')


    def updateEvents(self):
        self.event_ids, self.events, self.last_event_id = self.db.extract_Events() #event_ids, names, greatest_event_id

    def updateComboBox(self):
        self.event_combobox.config(values=self.events)



    def endEvent(self, dict):
        self.db.write_Event(str(self.last_event_id+1),self.event, dict)
        print(dict, 'written!')

    def chooseEvent(self):
        new_root = tk.Tk()
        print(self.last_event_id)
        event_combobox = ttk.Combobox(new_root, values=self.events)
        event_combobox.pack(pady=20, padx=20, anchor='nw')
        #self.event_combobox.bind("<<ComboboxSelected>>", self.load_event)

        def on_ok():
            selected_event = event_combobox.get()
            selected_event_id = self.event_ids[event_combobox.current()]
            print(self.event_ids)
            sauces, amounts = self.load_event(selected_event, selected_event_id)
            event_data = {}
            for sauce, amount in zip(sauces, amounts):
                event_data[sauce] = int(amount)
            sp = SaucePage(master=tk.Tk(), event_name=selected_event, db=self.db, event_id = selected_event_id, saucesList=self.sauces, parent=self, flag=True, amountList= event_data)
            sp.open()
            new_root.destroy()
            

        ok_button = tk.Button(new_root, text="OK", command=on_ok)
        ok_button.pack(pady=10)

        new_root.bind("<Return>", lambda event: on_ok())

        ok_button.focus_set()

    def plot_month(self):
        self.ax.clear()
        x = np.random.randint(0,10,10)
        y = np.random.randint(0,10,10)
        self.ax.plot(x, y)
        self.canvas.draw()

    def load_in_event(self, event=None):
        self.ax.clear()
        sauces, amounts = self.load_event(self.event_combobox.get(), self.event_ids[self.event_combobox.current()])
        cmap = mpl.colormaps['rainbow']
        colors = cmap(np.linspace(0, 1, len(sauces)))
        bars = self.ax.bar(sauces, amounts, color=colors)

        for i, value in enumerate(amounts):
            self.ax.text(i, value, str(value), ha='center', va='bottom')
        
        self.ax.set_xticks([])
        self.ax.set_xticklabels([])
        plt.gca().set_xticks([])
        self.ax.legend(bars,sauces,loc='center left', bbox_to_anchor=(1, 0.5),fontsize='small')
        self.fig.tight_layout()
        self.canvas.draw()


    def on_close(self):
        plt.close(self.fig)
        self.master.destroy()

    def open_event_window(self):
        new_root = tk.Tk()
        new_root.title("Enter Event Name")

        width = 600
        height = 400

        screen_width = new_root.winfo_screenwidth()
        screen_height = new_root.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        new_root.geometry(f'{width}x{height}+{x}+{y}')

        custom_font = font.Font(size=14)

        self.input = tk.Entry(new_root , font=custom_font, width=30)
        self.input.pack(pady=20)

        button = tk.Button(new_root , text="OK", width=20, height=2, font=custom_font, command=lambda: self.callback(new_root))
        button.pack(pady=10)


    def callback(self, master):
        text = self.input.get() 
        master.destroy()
        self.event = text
        new_root = tk.Tk()
        sp = SaucePage(master=new_root, event_name=self.event, db = self.db, parent=self, saucesList=self.sauces, event_id=self.last_event_id)
        sp.open()

    def load_event(self, event_name, event_id):
        print(self.event_combobox.current())
        print("Event Name and type", event_name, event_id, type(event_name), type(event_id))
        file = self.db.search_Event(event_name, event_id)
        print(file)
        data = json.loads(file)
        sauces = []
        amounts = []
        for key,value in data.items():
            sauces.append(key)
            amounts.append(value)
        return sauces, amounts
    
    def add_sauce(self, sauce_name):
        self.db.add_sauce(sauce_name)
        self.sauces = self.db.extract_sauces()

    def add_sauce_window(self):
        new_root = tk.Tk()
        new_root.title("Enter Sauce Name")

        width = 600
        height = 400

        screen_width = new_root.winfo_screenwidth()
        screen_height = new_root.winfo_screenheight()

        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        new_root.geometry(f'{width}x{height}+{x}+{y}')

        custom_font = font.Font(size=14)

        input = tk.Entry(new_root , font=custom_font, width=30)
        input.pack(pady=20)

        button = tk.Button(new_root , text="OK", width=20, height=2, font=custom_font, command=lambda: self.callback_add_sauce(new_root, input))
        button.pack(pady=10)

    def callback_add_sauce(self, master, input):
        text = input.get()
        self.add_sauce(text)
        master.destroy()

        


    
        

    