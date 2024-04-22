import tkinter as tk
from GUI.Sauce_Page import SaucePage


class LandingPage:
    def __init__(self, master):
        self.master = master
        master.title("Simple GUI")
        SaucesPage = SaucePage(master)
        self.label = tk.Label(master, text="Hello, GUI!")
        self.label.pack()

        self.button = tk.Button(master, text="Click Me!", command=self.say_hello)
        self.button = tk.Button(master, text="Sauce window!", command=SaucesPage.open)
        self.button.pack()

    def say_hello(self):
        print("Hello, button clicked!")    

    