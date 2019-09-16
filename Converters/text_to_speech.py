# __author__ == "Priya"

import os
from tkinter import *
import pygame as pg
from gtts import gTTS
import tkinter.scrolledtext as stext

MP3_FILE = "speech.mp3"

class TextToSpeech(Frame):
    def convert_text_to_speech(self):
        get_text = self.Text.get("1.0", END)
        language='en'
        audio = gTTS(text=get_text, lang=language, slow=False)
        audio.save(MP3_FILE)

    def play(self):
        self.convert_text_to_speech()
        pg.mixer.init()
        pg.mixer.music.load(MP3_FILE)
        pg.mixer.music.play()

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.Text = stext.ScrolledText(master)
        self.Text['font'] = ('consolas', '12')
        self.Text.pack(expand=True, fill=X, pady=20, padx=2)
        self.button = Button(master, text="Play", fg="white", bg="blue", command=self.play, height=2, width=8)
        self.button.pack()

root = Tk()
app = TextToSpeech(master = root)
app.master.geometry("500x540")
app.mainloop()
