# ####################### overriding ###################

# class Human:
#     def __init__(self,name=""):
#         self.name = name
#
#     def speak(self):
#         print(f"my name is {self.name}")
#
#
# class Employee(Human):
#     def __init__(self, empanme,email):
#         super(Employee, self).__init__(empanme)
#         self.email = email
#
#     def speak(self):
#         # super(Employee, self).speak()
#         super().speak()
#         print(f"My email is {self.email}")
#
#
# e = Employee("noha", "n@gmail.com")
# e.speak()

######################## Overloading ################################
class Student:
    def __init__(self, name, grade, level):
        self.name= name
        self.grade = grade
        self.level = level

    def speak(self, lang:str, country=None):
        if lang:
            print(f"my name is {self.name} I can speak {lang} ")
        if country:
            print(f"my name is {self.name} I can speak {lang} {country}")


    ## operator overlaoadin

    # def speak(self, lang:int):
    #     print(f"my name is {self.name} I can speak {lang} ##################")


s= Student("noha",100, 1)
s.speak("biiiii")
s.speak("biiiii", "USA")