# from random import randint
# from tkinter import *
#
# win = Tk()
# win.geometry("200x100")
#
# son = randint(100, 700)
# son2 = randint(200, 400)
#
# a = f"{son}x{son2}+{son}+{son2}"
#
# def kop():
#     for i in range(0, 200):
#         lev = Toplevel()
#         lev.geometry(a)
#
# top = Toplevel()
#
# def f():
#     top.geometry("200x100")
#     Label(top, text="Hello world").pack()
#
#
# but = Button(win, text="Click me", command=kop)
#
# but.pack()
# win.mainloop()


# from tkinter import *
# from PIL import Image, ImageTk
#
# win = Tk()
# img = Image.open("hero.png")
# imgtk = ImageTk.PhotoImage(img)
# lb = Label(win, image=imgtk)
#
# lb.pack()
# win.mainloop()






# from tkinter import *
# from PIL import Image, ImageTk
#
# win = Tk()
# win.title("Photo")
# win.geometry("400x500")
#
# img = Image.open("photo_2023-09-27_08-51-36.jpg")
# imgtk = ImageTk.PhotoImage(img)
#
# def photo():
#     top = Toplevel()
#     top.title("That's astonishing")
#     top.geometry("400x250+400+250")
#     lb2 = Label(top, text="Absolutely world class", bg="red")
#     lb = Label(top)
#     lb.config(image=imgtk)
#     lb2.pack()
#     lb.pack()
#
# but = Button(win, text="Messiii", bg="grey", command=photo)
#
# lab = Label(win, text="Here he is again")
#
# lab.pack()
# but.pack()
# win.mainloop()



# from tkinter import *
#
# from PIL import Image, ImageTk
#
#
#
# win = Tk()
#
# win.title("Welcome")
# win.geometry("350x400+500+300")
#
# img = Image.open("photo_2023-09-27_08-51-36.jpg")
# photo = ImageTk.PhotoImage(image=img)
#
# def get_photo():
#     surname = ent.get()
#     name = ent2.get()
#     top = Toplevel()
#
#     lab = Label(top, text=f"Your surname:{surname}\n"
#                           f"Your name:{name}")
#     lab2 = Label(top)
#     lab2.config(image=photo)
#
#     lab.pack()
#     lab2.pack()
#
# ent = Entry(win, bg="grey", bd=5, width=20,
#             font="consolas 20")
#
# ent2 = Entry(win, bg="grey", font="consolas 20",
#              width=20, bd=5)
#
# lb = Label(win, text="1:Surname\n"
#                      "2:Name",
#            font="times 25", height=5, width=20
#            )
#
# but = Button(win, text="Let's go", font="consolas 20",
#              bd=10, fg="black", width=15,
#              command=get_photo)
#
#
# lb.pack()
# ent.pack()
# ent2.pack()
# but.pack()
#
# win.mainloop()

