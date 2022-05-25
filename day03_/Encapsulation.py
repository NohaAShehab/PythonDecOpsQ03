'''

    Access modifiers ---> limit the accessibility of the properties
    public
    private
    protected
    static
    ####################### in python
    no access modifiers (keywords)
    static ---> class variable
    private :  __varname ====> private variable (property)
    protected: _varname ===> protected property

'''

# class Employee:
#     count =0  # like static variables in the other programming
#     def __init__(self,name,email, salary):
#         self.name = name
#         self._email = email  # protected --> can be accessed only in the class or the derived class
#         self.__salary =salary  # private --> can be accessed only inside the class
#         Employee.count +=1
#
#
# e =Employee("ahmed", "a@gmail.com", 100)
# # e._email = "ahmed@iti.gov.eg"  # ethically not allowed
# # private property
# print(e.__salary)  # AttributeError: 'Employee' object has no attribute '__salary'
# # e.__salary = 100000
# # print(e.__salary)

# ########################################################################################
"""
Apply certain logic on the input parameters 
"""


# class Employee:
#     count = 0  # like static variables in the other programming
#
#     def __init__(self, name, email, salary):
#         self.name = name
#         self._email = email  # protected --> can be accessed only in the class or the derived class
#         self.__salary = salary  # private --> can be accessed only inside the class
#         Employee.count += 1
#
#     # def getsal(self):
#     #     return self.__salary * .8
#     @property
#     def salary(self):
#         return self.__salary*.8
#
#     @salary.setter
#     def salary(self, sal):
#         if isinstance(sal, int):
#             self.__salary = sal
#         else:
#             self.__salary = 10000
#
#
#     # def setSal(self, sal):
#     #     if isinstance(sal, int):
#     #         self.__salary = sal
#     #     else:
#     #         self.__salary = 10000
#
#
# e = Employee("noha", "n", 2000000000000)
# print(e.salary)
# # e.setSal("333333333")
# e.salary = "iti"
#
#
# e2 = Employee("ahmed", "a", "iti")
# print(e2.salary)
###########################################################
class Employee:
    count = 0  # like static variables in the other programming

    def __init__(self, name, email, salary):
        self.name = name
        self._email = email  # protected --> can be accessed only in the class or the derived class
        self.salary = salary  # private --> can be accessed only inside the class
        Employee.count += 1

    @property
    def salary(self):
        return self.__salary*.8

    @salary.setter
    def salary(self, sal):
        if isinstance(sal, int):
            self.__salary = sal
        else:
            self.__salary = 10000


    # def setSal(self, sal):
    #     if isinstance(sal, int):
    #         self.__salary = sal
    #     else:
    #         self.__salary = 10000


e = Employee("noha", "n", 2000000000000)
print(e.salary)
# e.setSal("333333333")
e.salary = "iti"


e2 = Employee("ahmed", "a", "iti")
print(e2.salary)


