# __author__ == "Priya"

import random
from tkinter import *


class Application(Frame):
    def popupwindow(self, msg, title):
        popup = Tk()
        popup.geometry('280x100+{}+{}'.format(int(root.winfo_reqwidth()/2),int(root.winfo_reqheight()/2)))
        popup.wm_title(title)
        l1 = Label(popup, text=msg)
        l1.pack(side='top', pady=10)
        ok = Button(popup, text='Okay', command=popup.destroy)
        ok.pack()
        popup.mainloop()

    def ok(self):
        rand_value = random.randrange(0,11)
        print(rand_value)
        if str(rand_value) == str(self.var.get()):
            self.popupwindow("Congratulations!! You Guessed it correctly!", "Hurray!!")
        else:
            self.popupwindow("Oops!! You guessed it wrong", "Sorry!!")

    def __init__(self, master):
        Frame.__init__(self, master)
        self.var = StringVar()
        label = Label(master, text="Guess a number between 0 and 10")
        label.grid(row=0, column=1)
        self.entry = Entry(textvariable=self.var, justify=CENTER)
        self.entry.grid(row=4, column=1, sticky=N, pady=2, ipadx=40)
        self.button = Button(master, text="Okay", height=2, width=5, fg='white', bg='blue', command=self.ok)
        self.button.grid(row=5, column=1)

root = Tk()
app = Application(master=root)
app.master.geometry('270x100+{}+{}'.format(int(root.winfo_reqwidth()/2), int(root.winfo_reqheight()/2)))
app.mainloop()
root.destroy()