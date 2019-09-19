# __author__ == "Priya"
from nltk.chat.util import Chat, reflections

pairs = [
    [r'hi|hey|hello',
     ["Hello","Hey there", "Hi",]
     ],
    [r'how are you ?',
     ["I am doing good", "I am good, Thanks!",]],
    [r'who are you ?',
     ["I am your virtual assistant, Teddy", "I am Teddy, a chat-bot",]],
    [r'what is your work ?',
     ['My work is to assist you.', 'To help you with information, I have.',]],
    [r'my name is (.*)',
     ['Hello %1, How are you today ?', 'Hi, %1 nice to meet you. I am Teddy',]],
    [r'quit',
     ["Bye take care. See you soon.", "Thanks for chatting, Bye for now."]],
]

def start_chat():
    print("Hi, I am Teddy and I am your chat-bot.\nPlease type lower case english sentences to start a conversation."
          "Type quit to leave.")
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    start_chat()