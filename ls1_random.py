# from random import randint


# def random_1():

#     a = randint(1, 10)
#     b = randint(1, 10)
#     result = a + b
#     wrongs = 0
#     rights = 0
#     command = int(input(f"{a} + {b}: "))
#     if command == result:
#         print("right")
#         rights += 1

#     if not command == result:
#         wrongs += 1
#         print("wrong")
#
#     if wrongs < 5:
#         random_1()
#
#     if wrongs > 5:
#         print(f"You lose\n"
#               f"Rights:{rights}\n"
#               f"Wrongs:{wrongs}")





# def random_2():
#     a = randint(1, 100)
#     b = randint(1, 100)
#     result = a + b
#     wrongs = 0
#     rights = 0
#     command = int(input(f"{a} + {b}: "))
#     if command == result:
#         print("right")
#         rights += 1
#     if not command == result:
#         wrongs += 1
#         print("wrong")

#     if wrongs < 5:
#         random_2()

#     if wrongs > 5:
#         print(f"You lose\n"
#               f"Rights:{rights}\n"
#               f"Wrongs:{wrongs}")

# def random_3():
#     a = randint(1, 1000)
#     b = randint(1, 1000)
#     result = a + b
#     wrongs = 0
#     rights = 0
#     command = int(input(f"{a} + {b}: "))
#     if command == result:
#         print("right")
#         rights += 1
#     if not command == result:
#         wrongs += 1
#         print("wrong")
#     if wrongs > 5:
#         print("You lose")

#     if wrongs < 5:
#         random_3()

#     elif wrongs > 5:
#         print(f"You lose\n"
#               f"Rights:{rights}\n"
#               f"Wrongs:{wrongs}")

# def run():
#     print("Assalomu aleykum oyinimizga xush kelibsiz\n"
#           "O'yin darajalari\n"
#           "1:Oson\n"
#           "2:O'rtacha\n"
#           "3:Qiyin")
#     com = int(input("O'yin darajasini tanlang: "))

#     if com == 1:
#         random_1()

#     elif com == 2:
#         random_2()

#     elif com == 3:
#         random_3()

# if __name__=="__main__":
#     run()


from random import *


# print(uniform(1,10))
# print(choice(cars))
# shuffle(cars)
# print(cars)
# print(sample(cars, k=3))

# def choice_2(data):
#     return data[randint(0,len(data) -1)]
# print(choice_2(cars))

# def shuffle_2(data):
#     test = []
#     while len(test) != len(data):
#         a = randint(0,len(data) - 1)
#         if data[a] not in test:
#             test.append(data[a])
#         else:
#             continue
#     return test

# print(shuffle_2(cars))

# def sample_2(data:list,k:str):
#     test = []
#     while len(test) != k:
#         a = randint(0,len(data) - 1)
#         if data[a] not in test:
#             test.append(data[a])
#         else:
#             continue
#     return test

# print(sample_2(cars,3))

# print("Umarali")
def mashina_oyin():
    cars = [
        "Malibu", "Cobalt", "Bugatti",
        "Spark", "Nexia", "Gentra",
        "Audi", "Jeep", "Ferrari",
        "Tesla"
    ]
    a = randint(0,len(cars) - 1)
    b = cars[a]
    print(f"Kompyuter tanlagan mashinaning nomi:{len(b)}ta xarfdan iborat")
    ur = 1
    while True:
        command = input(">>>")
        if command != b:
            print("Notogri")
            ur += 1
        elif command == b:
            print(f"Javobingiz togri\n"
                  f"urunishlar:{ur}")
            break

print(mashina_oyin())





