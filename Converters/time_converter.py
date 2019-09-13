# __author__ == "Priya"

import tkinter
from tkinter import *
from tkinter import ttk
import pendulum


class TimeConverter(Frame):
    def get_time(self):
        from_tz = self.timezone_menu1.get()
        to_tz = self.timezone_menu2.get()
        from_time=pendulum.now(from_tz)
        to_time=from_time.in_timezone(to_tz)
        fmt="%Y-%m-%d %H:%M:%S"
        self.time_var1.set(from_time.strftime(fmt))
        self.time_var2.set(to_time.strftime(fmt))
        from_tz_val=pendulum.datetime(2000,1,1,tz=from_tz)
        to_tz_val=pendulum.datetime(2000,1,1,tz=to_tz)
        diff=from_tz_val.diff(to_tz_val).in_minutes()
        hours=divmod(diff,60)
        min=divmod(hours[1],1)
        label_text="The difference between two timezones is {} hours {} minutes".format(hours[0], min[0])
        Label(self.master,text=label_text).grid(row=6,column=4, columnspan=3)

    def __init__(self, master):
        Frame.__init__(self, master)
        self.time_var1 = StringVar()
        self.time_var2 = StringVar()
        self.entry1 = Entry(master, textvariable=self.time_var1)
        self.entry1.grid(row = 1, column = 4, ipadx=10, ipady=4,padx=20,pady=3)
        self.entry2 = Entry(master, textvariable=self.time_var2)
        self.entry2.grid(row=2, column=4, ipadx=10, ipady=4,padx=20,pady=3)
        self.time_var1.set('')
        self.time_var2.set('')
        timezones = pendulum.timezones
        self.timezone_menu1 = ttk.Combobox(master, values=timezones)
        self.timezone_menu1.grid(row=1, column=6, padx=20, pady=5, ipadx=10, ipady=4)
        self.timezone_menu2 = ttk.Combobox(master, values=timezones)
        self.timezone_menu2.grid(row=2, column=6, padx=20, pady=5, ipadx=10, ipady=4)
        self.button = Button(master, fg="white", bg="blue", text="Ok", command=self.get_time)
        self.button.grid(row=3, column=5)

root = Tk()
app = TimeConverter(master=root)
app.mainloop()

