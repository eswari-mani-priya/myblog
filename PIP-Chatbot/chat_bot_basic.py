# __author__ == "Priya"
from nltk.chat.util import Chat, reflections
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import time


pairs = [
        [r'hi|hey|hello',
         ["Hello", "Hey there", "Hi", ]
         ],
        [r'how are you ?',
         ["I am doing good", "I am good, Thanks!", ]],
        [r'who are you ?',
         ["I am your virtual assistant, Teddy", "I am Teddy, a chat-bot", ]],
        [r'what is your work ?',
         ['My work is to assist you.', 'To help you with information, I have.', ]],
        [r'my name is (.*)',
         ['Hello %1.upper(), How are you today ?', 'Hi, %1.upper() nice to meet you. I am Teddy', ]],
        [r'quit',
         ["Bye take care. See you soon.", "Thanks for chatting, Bye for now."]],
    ]

class Application(Frame):
    def onclick(self, event):
        chat=Chat(pairs, reflections)
        user_input = self.usr_input.get()
        self.usr_input.delete(0, END)
        response = chat.respond(user_input)
        self.conversation['state'] = 'normal'
        self.conversation.insert(END, "Human: " + user_input + "\n" + "Teddy: " + str(response)+"\n")
        self.conversation["state"] = "disabled"
        time.sleep(0.5)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.title = "Chatbot"
        # self.respond = Button(self, text='Get Response', command=self.onclick)
        # self.respond.grid(column=0, row=0, sticky='nesw', padx=3, pady=3)

        self.usr_input = Entry(self, state='normal')
        self.usr_input.grid(column=0, row=0, columnspan=2, sticky='nesw', padx=3, pady=3)
        self.usr_input.bind('<Return>', self.onclick)

        self.conversation_lbl = Label(self, anchor=E, text='Conversation:')
        self.conversation_lbl.grid(column=0, row=1, sticky='nesw', padx=3, pady=3)

        self.conversation = ScrolledText(self, state='normal')
        self.conversation.insert(END,"Teddy: Hi, I am Teddy and I am your chat-bot.\n"
                                     "Please type lower case english sentences to start a conversation.Type quit to leave.\n")
        self.conversation['state']='disabled'
        self.conversation.grid(column=0, row=2, columnspan=2, sticky='nesw', padx=3, pady=3)


root = Tk()
app = Application(master=root)
app.mainloop()