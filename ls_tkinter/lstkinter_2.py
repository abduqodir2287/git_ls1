# from tkinter import *
#
# win = Tk()
# win.title("Welcome to my site")
# win.config(bg="yellow")
# win.geometry("600x400+400+200")
#
# ontab = True
#
# def main():
#     count = 0
#     global bt, ontab
#     if ontab:
#         bt.config(text="ON", bg="green")
#         ontab = False
#
#     else:
#         bt.config(text="OFF", bg="red")
#         ontab = True
#
# lb = Label(win)
#
# bt = Button(win,
#             text="OFF", bg="red", bd=10,
#             fg="blue", font=("times"),
#             height=5, width=20,
#             command=main)
#
#
# bt.pack()
# win.mainloop()


# from tkinter import *
#
# ontab = True
# count = 0
# def main():
#     global ontab, lb, count
#
#     if ontab:
#         ontab = False
#         lb.config(text=f"{count}")
#         but.config(text="Subhanalloh")
#         count += 1
#     else:
#         ontab = True
#         lb.config(text=f"{count}")
#         but.config(text="Subhanalloh")
#         count += 1
#
#
# win = Tk()
# win.title("Welcome to my site")
# win.config(bg="yellow")
# win.geometry("400x400+500+250")
#
# lb = Label(win,
#            text=0, bd=5, fg="red",
#            font=("times"), height=3, width=20)
#
# but = Button(win, text="Ready", bd=5,
#              bg="red", font=("times"),
#              fg="green", height=3, width=15,
#              activebackground="green", activeforeground="red",
#              command=main)
#
#
# lb.pack()
# but.pack()
# win.mainloop()

# from tkinter import *
#
# ontab = True
# count = 0

# def main():
#     global count, ontab
#     if ontab == True:
#         ontab = False
#         count += 1
#         lb.config(text=f"{count}")
#     else:
#         ontab == True
#         count += 1
#         lb.config(text=f"{count}")
#
#
# rooot = Tk()
#
# rooot.title("Welcome to my site!!")
# rooot.config(bg="yellow")
# rooot.geometry("400x300+400+250")
#
# lb = Label(rooot,
#            text=0, bg="brown", fg="white",
#            font="times", height=3, width=20)
#
# but = Button(rooot,
#              text="Click", bd=5, bg="green", fg="red",
#              font="italic", height=3, width=15,
#              activeforeground="green", activebackground="red",
#              command=main)
#
#
# lb.pack()
# but.pack()
# rooot.mainloop()






