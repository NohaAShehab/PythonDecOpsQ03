# class Human:
#     pass
#
#
# ######### to make object from class
# n = Human()
# print(type(n))  # object from human
####################################################

# e1 = {
#     "name": "Ahmed",  # string
#     "email": "ahmed@gmail.com",  # string
#     "salary": 1000 # int
# }
# e2 = {
#     "name": "Ali",
#     "email": "ali@gmail.com",
#     "salary": 1000
# }
#
# e3 = {
#     "name": "Mostafa",
#     "email": "mostafa@gmail.com",
#     "salary": 1000
# }


# class Employee:
#     pass
#
#
# e1 = Employee()
######################################
# class Employee:
#     # define properties for the classes
#     def __init__(self):   # constructor function , this function will be called while creating the
#         # object
#         # print("the object is being created here")
#         print(self)  # refer to the memory location of the object
#         pass
#
#
# e1 = Employee()
# e2= Employee()
# ###################################################
# class Employee:
#     # define properties for the classes
#     def __init__(self,empname, empemail, empsal):
#         # their values depends on the instance
#         # name, email , salary ---> instance variables
#         self.name = empname
#         self.email = empemail
#         self.salary = empsal
#
#
# e1 = Employee("Ahmed", "ahmed@gmail.com", 1000)
# print(e1.__dict__)  # represent the instance properties in form of dictionary
# e2 = Employee("Mohamed", "moha@gmail.com", 2000)
# print(e2.__dict__)


# class Employee:
#     # define properties for the classes
#     def __init__(self,empname="", empemail="", empsal=0):
#         # their values depends on the instance
#         # name, email , salary ---> instance variables
#         self.name = empname
#         self.email = empemail
#         self.salary = empsal
#
#
# e1 = Employee("Ahmed", "ahmed@gmail.com", 1000)
# print(e1.__dict__)  # represent the instance properties in form of dictionary
# e2 = Employee("Mohamed", "moha@gmail.com", 2000)
# print(e2.__dict__)
# e3 = Employee()
# print(e3.__dict__)
# e4 = Employee("omar")
# print(e4.__dict__)
####################################################################
# class Employee:
#     # define properties for the classes
#     def __init__(self,empname="", empemail="", empsal=0):
#         # their values depends on the instance
#         # name, email , salary ---> instance variables
#         self.name = empname
#         self.email = empemail
#         self.salary = empsal
#
#
# e1 = Employee("Ahmed", "ahmed@gmail.com", 1000)
# # modify the instance variable of the instance
# e1.name = "AhmedMohamed"
# print(e1.__dict__)
# print(e1.email)
# ################################Instance method ####################################

# class Employee:
#     # define properties for the classes
#     def __init__(self, empname="", empemail="", empsal=0):
#         # their values depend on the instance
#         # name, email , salary ---> instance variables
#         """ __init__ special method --> is called when you create an object from the class"""
#         self.name = empname
#         self.email = empemail
#         self.salary = empsal
#
#     # ### instance method ---> represent object capability
#     def speak(self):
#         print(f"I am {self.name} you can reach me at {self.email}")
#
#
# e1 = Employee("Ahmed", "ahmed@gmail.com", 1000)
# e1.speak()
# e2 = Employee("mohamed", "mm")
# e2.speak()
# ##################### class variable #####################################################
# class Employee:
#     # # define common property for the class instances
#     # class variable  --> represent common value shared between all class instances
#     # class variable can be modified through the class name, and any change in the class variable
#     # will affect the previous and the upcoming created object
#     tax = .14
#     count = 0
#
#     # define properties for the classes
#     def __init__(self, empname="", empemail="", empsal=0):
#         self.name = empname
#         self.email = empemail
#         self.salary = empsal
#         Employee.count +=1
#
#     # ### instance method ---> represent object capability
#     def speak(self):
#         print(f"I am {self.name} you can reach me at {self.email}")
#
#
# e1 = Employee("Ahmed", "ahmed@gmail.com", 1000)
# # e2 = Employee("mohamed", "mm")
# # print(Employee.tax)
# # Employee.tax = .1

############################################################################
##################### class method #####################################################
# class Employee:
#     tax = .14
#     count = 0
#
#     # define properties for the classes
#     def __init__(self, empname="", empemail="", empsal=0):
#         self.name = empname
#         self.email = empemail
#         self.salary = empsal
#         Employee.count +=1
#
#     # ### instance method ---> represent object capability
#     def speak(self):
#         print(f"I am {self.name} you can reach me at {self.email}")
#
#     # class method
#     @classmethod
#     def getEmpCount(cls):
#         # cls ---> represent the class
#         # print(Employee.count)
#         print(cls.count)
#
#     # ### object factory ### cls ---> represent the class
#     @classmethod
#     def createEmp(cls, username):
#         return cls(username, "emp@iti.com", 1000)
#
#     @classmethod
#     def addEmployees(cls, emp1, emp2):
#         if isinstance(emp1, Employee) and isinstance(emp2, Employee):
#             return cls(f"{emp1.name} {emp2.name}",f"{emp1.email}", emp1.salary+emp2.salary)
#
#         return None
#
#
#
#
# e1 = Employee("Ahmed", "ahmed@gmail.com", 1000)
# Employee.getEmpCount()
# e3 = Employee.createEmp("noha")
#
# e4= Employee.addEmployees(e1,e3)
# #################################### static methods #########################

class Employee:
    tax = .14
    count = 0

    def __init__(self, empname="", empemail="", empsal=0):
        self.name = empname
        self.email = empemail
        self.salary = empsal  # gross
        Employee.count +=1

    # ### instance method ---> represent object capability
    def speak(self):
        print(f"I am {self.name} you can reach me at {self.email} {Employee.netsal(self.salary)}")

    # ### object factory ### cls ---> represent the class
    @classmethod
    def createEmp(cls, username):
        return cls(username, "emp@iti.com", 1000)

    @staticmethod   # as helper method
    def netsal(sal):
        return sal * .8


e1 = Employee("Ahmed", "ahmed@gmail.com", 1000)
print(Employee.netsal(e1.salary))
print(Employee.netsal(1000000))
#
# def netsal(sal):
#     return sal*.8
#
# e1_netsal = netsal(e1.salary)
# print(e1_netsal)
#
# print(netsal(10000))

















