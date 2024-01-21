import webbrowser
from tkinter import *


def search():
    url = URL.get()
    webbrowser.open(url)

root = Tk()
root.title("كحيانbrowser")
root.geometry("400x400")

intro = Label(text="Enter the URL - أدخل اللينك")
intro.pack()

URL = Entry(root)
URL.pack()

enter = Button(text="Enter", command=search)
enter.pack()


root.mainloop()