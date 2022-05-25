
# #################### inheritance
# class Human:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
#
# class Employee(Human):
#     pass
#
# e = Employee("noha")
# e.speak()

# #####################################################

# class Human:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
#
# class Employee(Human):
#     def __init__(self, email):
#         self.email = email
#
# e = Employee("noha@iti.com")
# e.speak()

###########################################################
# class Human:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
#
# class Employee(Human):
#     def __init__(self, empname, email):
#         # call parent constructor
#         super().__init__(name=empname)
#         self.email = email
#
#
# e = Employee("noha","noha@iti.com")

################################################3
class A:
    def __init__(self):
        self.aaaa = "a"
    pass

class B:
    def __init__(self):
        self.test = "b"

class C(A,B):
    def __init__(self):
        super().__init__()  #A
        B.__init__(self)



c = C()





