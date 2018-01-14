from tkinter import *


class WellRested:
    def __init__(self, master):
        frame = Frame(master, width=400, height=400)
        frame.pack()
        topMenu = Menu(master)
        master.config(menu=topMenu)

        fileMenu = Menu(topMenu)
        topMenu.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="New", command=print)
        fileMenu.add_command(label="Home", command=print)
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=master.quit)

        windowMenu = Menu(topMenu)
        topMenu.add_cascade(label="Window", menu=windowMenu)
        windowMenu.add_command(label="Minimize", command=print("Minimize"))

