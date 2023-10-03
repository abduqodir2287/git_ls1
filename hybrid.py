# class Gfather:
#     def __init__(self,grandfathername:str):
#         self.grandfathername = grandfathername
#
#
#     def f1(self):
#         print("This func from "
#               "Gfather class")
#
# class Gmother:
#
#     def __init__(self,grandmothername:str):
#         self.grandmothername = grandmothername
#
#
#     def f2(self):
#         print("This func from "
#               "Gmother class")
#
# class Uncle(Gfather,Gmother):
#
#     def __init__(self,unclename:str,grandfathername,grandmothername):
#         self.unclename = unclename
#
#         Gfather.__init__(self,grandfathername)
#         Gmother.__init__(self,grandmothername)
#
#     def f3(self):
#         print("This func from "
#               "Uncle class")
#
# class Father(Gfather):
#
#     def __init__(self,fathername:str,grandfathername):
#         self.fathername = fathername
#         Gfather.__init__(self,grandfathername)
#
#
#     def f4(self):
#         print("This func from "
#               "Father class")
#
# class Son1(Father):
#
#     def __init__(self,son1name:str,fathername,grandfathername):
#         self.son1name = son1name
#
#         Father.__init__(self,fathername,grandfathername)
#
#     def f5(self):
#         print("This func from"
#               " Son1 class")
#
# class Son2(Father):
#
#     def __init__(self, son2name: str, fathername, grandfathername):
#         self.son2name = son2name
#
#         Father.__init__(self, fathername, grandfathername)
#
#     def f6(self):
#         print("This func from"
#               " Son2 class")



# obj1 = Gfather()
# obj1.f1()
# obj2 = Gmother()
# obj2.f2()
# obj3 = Uncle("Ali","Ahmad","Nasiba")
# obj3.f1()
# obj3.f2()
# obj3.f3()
# obj4 = Father("Umar","Ahmad")
# obj4.f1()
# obj4.f4()
# obj5 = Son1("Salohiddin", "Umar", "Ahmad")
# obj5.f1()
# obj5.f4()
# obj5.f5()
# obj6 = Son2("Komil", "Umar", "Ahmad")
# obj6.f1()
# obj6.f4()
# obj6.f6()


