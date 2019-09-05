# __author__ == "Priya"

from tkinter import *


class Application(Frame):
    def press(self, num):
        self.value = self.value + str(num)
        self.contents.set(self.value)

    def equalpress(self):
        try:
            result = str(eval(self.value))
            self.contents.set(result)
            self.value = ""
        except:
            self.contents.set("error")
            self.value = ""

    def clearvalue(self):
        self.value=""
        self.contents.set("")

    def get_widgets(self, master):
        self.button1 = Button(master, text='1', height=2, width=6, command=lambda: self.press(1), fg="white", bg="blue")
        self.button1.grid(row=1, column=0)
        self.button2 = Button(master, text='2', height=2, width=6, command=lambda: self.press(2), fg="white", bg="blue")
        self.button2.grid(row=1, column=1)
        self.button3 = Button(master, text='3', height=2, width=6, command=lambda: self.press(3), fg="white", bg="blue")
        self.button3.grid(row=1, column=2)
        self.button4 = Button(master, text='4', height=2, width=6, command=lambda: self.press(4), fg="white", bg="blue")
        self.button4.grid(row=2, column=0)
        self.button5 = Button(master, text='5', height=2, width=6, command=lambda: self.press(5), fg="white", bg="blue")
        self.button5.grid(row=2, column=1)
        self.button6 = Button(master, text='6', height=2, width=6, command=lambda: self.press(6), fg="white", bg="blue")
        self.button6.grid(row=2, column=2)
        self.button7 = Button(master, text='7', height=2, width=6, command=lambda: self.press(7), fg="white", bg="blue")
        self.button7.grid(row=3, column=0)
        self.button8 = Button(master, text='8', height=2, width=6, command=lambda: self.press(8), fg="white", bg="blue")
        self.button8.grid(row=3, column=1)
        self.button9 = Button(master, text='9', height=2, width=6, command=lambda: self.press(9), fg="white", bg="blue")
        self.button9.grid(row=3, column=2)
        self.button0 = Button(master, text='0', height=2, width=6, command=lambda: self.press(0), fg="white", bg="blue")
        self.button0.grid(row=4, column=0)
        self.eq = Button(master, text='=', height=2, width=6, command=lambda: self.equalpress(), fg="white", bg="blue")
        self.eq.grid(row=4, column=1)
        self.clr = Button(master, text='Clear', height=2, width=6, command=lambda: self.clearvalue(), fg="white", bg="blue")
        self.clr.grid(row=4, column=2)
        self.add = Button(master, text='+', height=2, width=6, command=lambda: self.press('+'), fg="white", bg="blue")
        self.add.grid(row=1, column=3)
        self.sub = Button(master, text='-', height=2, width=6, command=lambda: self.press('-'), fg="white", bg="blue")
        self.sub.grid(row=2, column=3)
        self.mul = Button(master, text='*', height=2, width=6, command=lambda: self.press('*'), fg="white", bg="blue")
        self.mul.grid(row=3, column=3)
        self.div = Button(master, text='/', height=2, width=6, command=lambda: self.press('/'), fg="white", bg="blue")
        self.div.grid(row=4, column=3)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.contents = StringVar()
        self.entry = Entry(textvariable=self.contents)
        self.contents.set("Enter your expression: ")
        self.value=""
        self.entry.grid(columnspan=4, ipadx=70, ipady=10, padx=5, pady=10)
        self.get_widgets(master)

root = Tk()
app = Application(master=root)
app.master.title("Generic Calculator")
app.master.configure(background='yellow')
app.mainloop()



