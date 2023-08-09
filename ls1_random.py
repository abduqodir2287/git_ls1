from random import randint


def random_1():

    a = randint(1, 10)
    b = randint(1, 10)
    result = a + b
    wrongs = 0
    rights = 0
    command = int(input(f"{a} + {b}: "))
    if command == result:
        print("right")
        rights += 1

    if not command == result:
        wrongs += 1
        print("wrong")

    if wrongs < 5:
        random_1()

    if wrongs > 5:
        print(f"You lose\n"
              f"Rights:{rights}\n"
              f"Wrongs:{wrongs}")





def random_2():
    a = randint(1, 100)
    b = randint(1, 100)
    result = a + b
    wrongs = 0
    rights = 0
    command = int(input(f"{a} + {b}: "))
    if command == result:
        print("right")
        rights += 1
    if not command == result:
        wrongs += 1
        print("wrong")

    if wrongs < 5:
        random_2()

    if wrongs > 5:
        print(f"You lose\n"
              f"Rights:{rights}\n"
              f"Wrongs:{wrongs}")

def random_3():
    a = randint(1, 1000)
    b = randint(1, 1000)
    result = a + b
    wrongs = 0
    rights = 0
    command = int(input(f"{a} + {b}: "))
    if command == result:
        print("right")
        rights += 1
    if not command == result:
        wrongs += 1
        print("wrong")
    if wrongs > 5:
        print("You lose")

    if wrongs < 5:
        random_3()

    elif wrongs > 5:
        print(f"You lose\n"
              f"Rights:{rights}\n"
              f"Wrongs:{wrongs}")

def run():
    print("Assalomu aleykum oyinimizga xush kelibsiz\n"
          "O'yin darajalari\n"
          "1:Oson\n"
          "2:O'rtacha\n"
          "3:Qiyin")
    com = int(input("O'yin darajasini tanlang: "))

    if com == 1:
        random_1()

    elif com == 2:
        random_2()

    elif com == 3:
        random_3()

if __name__=="__main__":
    run()







