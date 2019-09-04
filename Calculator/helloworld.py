# __author__ == "Priya"

from tkinter import *


class App(Frame):
    def say_welcome(self):
        print("Welcome to my first Tkinter app!!")

    def getWidgets(self):
        self.EXIT = Button(self)
        self.EXIT["text"] = "Quit"
        self.EXIT["bg"] = "yellow"
        self.EXIT["fg"] = "blue"
        self.EXIT["command"] = self.quit
        self.EXIT.pack({'side':'left'})
        self.welcome = Button(self)
        self.welcome["text"] = "Welcome"
        self.welcome["bg"] = "yellow"
        self.welcome["fg"] = "green"
        self.welcome["command"] = self.say_welcome
        self.welcome.pack({"side":"left"})

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.getWidgets()


root = Tk()
app = App(master=root)
app.mainloop()
root.destroy()
