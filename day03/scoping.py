print("---------- Global scope --------")
""" any variable defined in the python script is defined in the global scope 
can be accessed anywhere inside the script for reading only 

"""
################################## (1) what is global ########################
# course = "Python"  # variable is defined in the global scope of the python file (module)
# print(course)
#
#
# course= "Python course"
#
# print(course)
# #########################  2- read(print) the value of the global variable inside the function##############################
# course = "Python"

# def test():
#     print(course)
#     print("hello world")
#     print("----------------------------------------")
#
# test()
# print(course)

# ####################### 3- modify the global variable from inside function ############################################
# name = "Ahmed"
#
# def modifyname():
#     ### modify the global variable "name"
#     global name
#     name = "Mohamed"
#     print(name)
#     print("----------------------------------")
# modifyname()
# print(name)
################################1- local scope definition ###################################################
print("---------- local scope --------")
"""Any variable defined inside the function --> is considered ti have local scope
---> local scope ---> variable can be accessed only inside the function you defined it in.

---> local scope variable can be read in the inner function of the outerfunction 
"""
#
# def askforname():
#     username = input("please enter your name ... :")
#     print(username)
#     print("---------------------------------------------------")
#
# askforname()
# print(username)  # username is not defined

# ############################### 2- inner function  --> read local variable ###############################
#
# def outerfunction():
#     course = "Python"
#
#     def myinnerfunction():
#         print("####################################")
#         print("I am the inner function")
#         print(f"course value = {course}")
#         print("####################################")
#
#     myinnerfunction()
#     print(f"course value = {course}")
#
# outerfunction()


############################### 3- inner function  --> modify local variable from the innerfunction ###############################

# def outerfunction():
#     course = "Python"
#
#     def myinnerfunction():
#         nonlocal course
#         course ="django"  # ## new local variable for the inner function
#         print("####################################")
#         print("I am the inner function")
#         print(f"course value = {course}")
#         print("####################################")
#
#     print(f"course value = {course}")
#     myinnerfunction()
#     print(f"course value = {course}")
#
# outerfunction()

########################################
grade = "pass"  # global scope

# def abc():
#     nonlocal grade
#     grade = "verygood"
#
# abc()
# print(grade)
# print(intake)
intake = 42










