from func import magazin, init

def onlayn_magazin():
    print("Assalomu aleykum onlayn dokonimizga xush kelibsiz |\n"
          "Buyriqlardan birini tanlang |\n"
          "1:Maxsulotlar xaqida malumot olish |\n"
          "2:Yordam |")
    command = int(input("Buyriq raqamini kiriting: "))
    print("-" * 25)
    if command == 1:
        print("Maxsulotlar |\n"
              "1:Coca cola |\n"
              "2:Fanta |\n"
              "3:Pepsi |\n"
              "4:Non |\n"
              "5:Qurt |")
        com = int(input("Buyriq raqamini kiriting: "))
        print("-" * 25)
        if com == 1:
            print("Coca cola |\n"
                  "Nomi:Coca cola\n"
                  "Xajmi:2.L\n"
                  "Narxi:15000 UZS\n"
                  "-----------------")

        elif com == 2:
            print("Fanta |\n"
                  "Nomi:Fanta\n"
                  "Xajmi:1.5.L\n"
                  "Narxi:12000 UZS\n"
                  "-----------------")

        elif com == 3:
            print("Pepsi |\n"
                  "Nomi:Pepsi\n"
                  "Xajmi:1.L\n"
                  "Narxi:9000 UZS\n"
                  "-----------------")
        elif com == 4:
            print("Non |\n"
                  "Nomi:Buxanka\n"
                  "Xajmi:600 gr\n"
                  "Narxi:2800 UZS\n"
                  "-----------------")
        elif com == 5:
            print("Qurt |\n"
                  "Nomi:Mega\n"
                  "Xajmi:15 gr\n"
                  "Narxi:500 UZS\n"
                  "-----------------"
                  )

    elif command == 2:
        print("Yordam |\n"
              "Siz bizning onlayn dokonimizda barcha korsatilgan\n"
              "maxsulotlar xaqida malumot olishingiz mumkin |\n")

    magazin()





if __name__ == "__main__":
    onlayn_magazin()



