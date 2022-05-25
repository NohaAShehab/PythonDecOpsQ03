class Employee:
    count = 0  # like static variables in the other programming

    def __init__(self, name, email, salary):
        self.name = name
        self._email = email  # protected --> can be accessed only in the class or the derived class
        self.salary = salary  # private --> can be accessed only inside the class
        Employee.count += 1

    @property
    def salary(self):
        return self.__salary * .8

    @salary.setter
    def salary(self, sal):
        if isinstance(sal, int):
            self.__salary = sal
        else:
            self.__salary = 10000

    def __str__(self):  # built-in magic function -->-must return with string
        return f"{self.name}"

    def __repr__(self):  # for developer
        return f"Employee(name={self.name}, email={self._email},salary={self.salary})"

    def __len__(self):  #must return with int
        return len(self.__dict__)

    def __call__(self, *args, **kwargs):
        print(f"{self} object called")


e = Employee("noha", "noha@iti.com", 10000)
print(e)  # check if the class has method __str__ --->run =
print(e.__repr__())
print(len(e))

e = Employee("Ahemd", "ahmed@iti.com", 10000)
print(e)  # check if the class has method __str__ --->run =
############################################
# class ABC(tuple):
#     pass
print(e())  #object is not callable

