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

        helpMenu = Menu(topMenu)
        topMenu.add_cascade(label="Help", menu=helpMenu)
        helpMenu.add_command(label="Getting Started")

        timeElapsedLabel = Label(frame, text="Time elapsed in current interval: 0:00:00:00")
        timeElapsedLabel.grid(row=0, column=0)
        timeRemainingLabel = Label(frame, text="Time remaining in current interval: 0:00:00:00")
        timeRemainingLabel.grid(row=1, column=0)
        createIntervalButton = Button(frame, text="Create a new rest interval", command=self.createInterval)
        createIntervalButton.grid(row=0, column=5)
        pauseIntervalButton = Button(frame, text="Pause the current interval")
        pauseIntervalButton.grid(row=1, column=5)
        resetIntervalButton = Button(frame, text="Reset the current interval")
        resetIntervalButton.grid(row=2, column=5)

    def createInterval(self):
        createIntervalFrame = Tk()
        promptLabel = Label(createIntervalFrame, text="Please select the type of interval you would like to create")
        promptLabel.grid(row=0)
        defaultButton = Button(createIntervalFrame, text="Default", command=self.beginDefault and createIntervalFrame.quit)
        defaultButton.grid(row=1, column=0)
        customButton = Button(createIntervalFrame, text="Custom", command=self.determineCustom and createIntervalFrame.quit)
        customButton.grid(row=1, column=1)
        createIntervalFrame.mainloop()

    def determineCustom(self):

        customFrame = Tk()

        customFrame.mainloop()

    def beginDefault(self):
        initialTime = 0



