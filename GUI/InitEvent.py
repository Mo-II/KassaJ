import tkinter as tk
from GUI.LandingPage import LandingPage
from tkinter import font

class InitEvent:
    def __init__(self, master):
        self.master = master
        master.title("Enter Event Name")

        
        self.center_window(600, 400)

        custom_font = font.Font(size=14)

        self.input = tk.Entry(master, font=custom_font, width=30)
        self.input.pack(pady=20)

        button = tk.Button(master, text="OK", width=20, height=2, font=custom_font, command=self.callback)
        button.pack(pady=10)

    def callback(self):
        text = self.input.get() 
        self.master.destroy()
        new_root = tk.Tk()
        LandingPage(new_root, text)
        new_root.mainloop()

    def center_window(self, width, height):
        # Get screen width and height
        screen_width = self.master.winfo_screenwidth()
        screen_height = self.master.winfo_screenheight()

        # Calculate position x, y
        x = (screen_width // 2) - (width // 2)
        y = (screen_height // 2) - (height // 2)

        self.master.geometry(f'{width}x{height}+{x}+{y}')




