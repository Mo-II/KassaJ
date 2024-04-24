import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from GUI.Sauce_Page import SaucePage


class LandingPage:
    def __init__(self, master):
        self.master = master
        master.title("Simple GUI")
        SaucesPage = SaucePage(master)
        self.buttonEvent = tk.Button(master, text="event", command=lambda : print("not implemented yet"))
        self.buttonEvent.grid(row=0,column=0)
        self.buttonWeek = tk.Button(master, text="week", command=lambda : print("not implemented yet"))
        self.buttonWeek.grid(row=0,column=1)
        self.buttonMonth = tk.Button(master, text="month", command=lambda : print("not implemented yet"))
        self.buttonMonth.grid(row=0,column=2)
        self.button = tk.Button(master, text="New event", command=SaucesPage.open)
        self.button.grid(row=5,column=10)
        self.plot_graph()

    def say_hello(self):
        print("Hello, button clicked!")    

    def plot_graph(self):
        # Sample data
        x = [1, 2, 3, 4, 5]
        y = [2, 3, 5, 7, 11]

        # Create a new figure
        fig = plt.Figure()

        # Plot the data
        plt.plot(x, y)

        # Create a Tkinter canvas
        canvas = FigureCanvasTkAgg(fig, master=self.master)
        canvas_widget = canvas.get_tk_widget()

        # Place the canvas on the Tkinter window
        canvas_widget.grid(row=1,column=0,columnspan=3, sticky="nsew")

    