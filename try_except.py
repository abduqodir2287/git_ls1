# a = input(">>>")
# try:
#     print(int(a) * int(a))
#
# except:
#     print(a.capitalize())

try:
    file = open("test.txt")
    file.write("nma gap")
    file.close()
except FileNotFoundError as e:
    print("Fayl mavjud emas")
    print(e)






