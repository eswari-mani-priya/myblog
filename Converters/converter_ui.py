# __author__ == "Priya"

from tkinter import *
from tkinter import ttk
import os
import sys
sys.path.append(os.path.abspath(__file__))
from currency_converter import CurrencyConverter



class Application(Frame):
    def popupwindow(self, msg):
        popup = Tk()
        popup.geometry('400x100+{}+{}'.format(int(root.winfo_reqwidth()/2), int(root.winfo_reqheight()/2)))
        popup.wm_title('Error!')
        label = Label(popup, text=msg)
        label.pack(side="top", pady=10)
        ack = Button(popup, text="Okay", command=popup.destroy)
        ack.pack()
        popup.mainloop()

    def ok(self):
        from_cur = self.from_menu.get()
        to_cur = self.to_menu.get()
        if (str(from_cur) != '') and (str(to_cur) != ''):
            try:
                convert_val = CurrencyConverter().convert_currency(from_cur, to_cur, self.from_val.get())
                self.to_val.set(convert_val)
            except:
                self.popupwindow('No conversion available for this pair in API!!')
        else:
            self.popupwindow("Please select both Currencies!")

    def resetval(self):
        self.from_menu.set('')
        self.to_menu.set('')
        self.from_val.set('1')
        self.to_val.set('')

    def __init__(self, master):
        Frame.__init__(self, master)
        # From Currency Variables
        choices = sorted(list(CurrencyConverter().get_currencies_data().keys()))
        self.from_menu = ttk.Combobox(master, values=choices)
        self.from_val = StringVar()
        self.from_entry = Entry(textvariable=self.from_val, justify=CENTER)
        self.from_val.set('1')
        self.from_entry.grid(row=1, column=1, ipadx=10, ipady=4)
        self.from_menu.grid(row=1, column=2, padx=20, pady=5, ipadx=10, ipady=4)
        self.to_menu = ttk.Combobox(master, values=choices)
        self.to_val = StringVar()
        self.to_entry = Entry(textvariable=self.to_val, justify=CENTER)
        self.to_val.set('')
        self.to_entry.grid(row=2, column=1, ipadx=10, ipady=4)
        self.to_menu.grid(row=2, column=2, padx=20, pady=5, ipadx=10, ipady=4)
        self.ok = Button(master, text="Convert", height=2, width=6, command=self.ok, bg='blue', fg='white')
        self.ok.grid(row=3, column=1, ipadx=70, ipady=2, pady=20)
        self.reset = Button(master, text="Reset", height=2, width=6, command=self.resetval, bg='blue', fg='white')
        self.reset.grid(row=3, column=2, ipadx=70, ipady=2, pady=20)

root = Tk()
app = Application(master=root)
app.master.geometry('500x200+{}+{}'.format(int(root.winfo_reqwidth()/2), int(root.winfo_reqheight()/2)))
app.master.title("Currency Converter")
app.mainloop()
root.destroy()