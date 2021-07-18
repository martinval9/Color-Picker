from tkinter import *
from tkinter import colorchooser as ColorChooser

def test():
    color = ColorChooser.askcolor(title="Elige un color")
    root.destroy()

root = Tk()
root.title("ColorPicker")
root.config(bg = "#000")
root.geometry("0x0")
root.resizable(0,0)
test()
root.mainloop()
