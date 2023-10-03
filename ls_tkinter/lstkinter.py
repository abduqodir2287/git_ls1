from random import *
from tkinter import *
from datetime import *


def uptime():
    now = datetime.now().strftime("Toshkentda Soat->%H:%M:%S")
    lb.config(text=f"{now}")
    lb.after(1000,uptime)

# def uptime():
#     but.config(text="Hi!")

root = Tk()

root.title("Welcome to the site of smiles")
root.config(bg="brown")
root.geometry("800x400+400+250")


def smile():
    sm = "😁😱❤🥳😘😂🤔🖕😡😋😀😇😘🥸😎😡🤯😶🤗😐🤮🤐😵💫🤓🎃💩🤠👹👌🙏🧠🧓💻"
    n = sample(sm, 1)
    lb.config(text=f"{n}")


lb = Label(root,
           text="Hello world❤️",
           fg="black", font=("times"),
           bg="yellow", height=5, width=20)

# lb.config(text=f"{uptime()}")

but = Button(root, text="Click here😅",
             bd=5, font="times", fg="yellow",
             bg="blue", height=5, width=15,
             command=smile)

lb.pack()
but.pack()
root.mainloop()





