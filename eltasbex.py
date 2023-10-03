# from tkinter import *
#
# ontab = True
# count = 0
#
# def al():
#     but.config(text="Alhamdulillah")
#
# def main_2():
#     lb.config(text=f"{count}")
#     but.config(text="Alhamdulillah")
#
# def main_3():
#     lb.config(text=f"{count}")
#     but.config(text="Alohuakbar")
#
#
# def main_1():
#     global count
#
#     if count < 33:
#         lb.config(text=f"{count}")
#         but.config(text="Subhanalloh")
#         count += 1
#     elif count < 33:
#         lb.config(text=f"{count}")
#         but.config(text="Subhanalloh")
#         count += 1
#
#     if count >= 33 and count <= 66:
#         lb.config(text=f"{count}")
#         but.config(text="Alhamdulillah")
#         count += 1
#
#     if count >= 66 and count <= 99:
#         lb.config(text=f"{count}")
#         but.config(text="Allohuakbar")
#         count += 1
#
#     if count > 99:
#         count = 0
#
#
#
# win = Tk()
# win.title("Welcome to my site")
# win.config(bg="yellow")
# win.geometry("400x400+500+250")
#
# lb = Label(win,
#            text=f"{count}", bd=5, fg="red",
#            font=("times"), height=3, width=20)
#
# but = Button(win, text="Ready", bd=5,
#              bg="red", font=("times"),
#              fg="green", height=3, width=15,
#              activebackground="green", activeforeground="red",
#              command=main_1)
#
#
# lb.pack()
# but.pack()
# win.mainloop()


from tkinter import *

count = 0

def main():
    global count
    if count <= 33 and count >= 0:
        count += 1
        lb.config(text=f"{count}")
        but.config(text="Subhanalloh")
    if count >= 33 and count <= 65:
        lb.config(text=f"{count}")
        but.config(text="Alhamdulillah")
        count += 1
    elif count >= 65 and count <= 99:
        lb.config(text=f"{count}")
        but.config(text="Allohuakbar")
        count += 1
    if count > 99:
        count = 0



win = Tk()
win.title("Welcome to my site")
win.config(bg="yellow")
win.geometry("500x400+400+250")
win.iconbitmap()

lb = Label(win,
           text="0",font=("times", 20),
           height=3, width=10)

but = Button(win,
             text="Subhanalloh", fg="red", bd=5,
             font="times", activebackground="red",
             activeforeground="green", height=3,
             width=15, command=main)


lb.pack()
but.pack()
win.mainloop()


