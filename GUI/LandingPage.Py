import tkinter as tk
class LandingPage:
    def __init__(self, master):
        self.master = master
        master.title("Simple GUI")

        self.label = tk.Label(master, text="Hello, GUI!")
        self.label.pack()

        self.button = tk.Button(master, text="Click Me!", command=self.say_hello)
        self.button.pack()

    