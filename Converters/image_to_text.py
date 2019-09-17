# __author__ == "Priya"
# __author__ == "Priya"
from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image
import pytesseract


class ImagetoText(Frame):
    def OpenFile(self):
        img = askopenfilename(initialdir="./",
                              filetypes=(("Image File", "*.jpg"), ("Image File", "*.png"), ("All Files", "*.*")),
                              title="Choose a file.")
        self.img = img

    def convert(self):
        value = pytesseract.image_to_string(Image.open(self.img))
        self.var.set(value)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.button = Button(master, text="Select Image", height=2, width=10, command=self.OpenFile)
        self.button.pack(padx=5, pady=2, ipadx=2, ipady=3)
        self.img = ''
        self.var = StringVar(master)
        self.entry = Entry(textvariable=self.var)
        self.entry.pack(fill=X, pady=10, ipady=50)
        self.ok = Button(master, text="Convert", width=5, fg="white", bg="blue", command=self.convert)
        self.ok.pack()

root=Tk()
app=ImagetoText(master=root)
app.master.geometry("400x250")
app.mainloop()