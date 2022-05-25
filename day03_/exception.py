# ######################## Exception handling ####################
# Exception
# print("-----------------------------------")
# x = 10
# print(x)
# print(name)  # runtime error ----> You handle it.
# print("##########################################")
# ######################################################

# def addnums(num1, num2):
#     return num1*num2
#
#
# m= addnums(2,2)
# print(m)
#
# n = addnums(4,5)
# print(n)

# ###########################################################
"""
Exception : any sudden action stop the script execution
### any event ---> occurs during the script execution --> disturb the normal flow the processing
"""


# name = "ttt"
# print('============ Exception handling')
# try:
#     print(name)
# except:
#     print("exception happeed")

# print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
################################################################


# num = input('please enter name')
# try:
#     num = int(num)
# except Exception as e:
#     print(e)
#     num = None
#
#
# print(num)

# def askfornum(message):
#     num = input(f'please enter {message}')
#     try:
#         num = int(num)
#         return num
#     except Exception as e:
#         return askfornum(message)
#
#
# n = askfornum('day')
# ###################################################

# grade = input("please enter your grade ")
# try:
#     grade = int(grade)
# except Exception as e:
#     print(e)
#     grade = None
# else:
#     # ## this block will be executed if there is no exception
#     print(grade)
#     print("No exception happened")


# def askfornum():
#     grade = input("please enter your grade ")
#     try:
#         grade = int(grade)
#     except Exception as abbass:
#         print(abbass)  # e---> error message
#         grade = None
#         return askfornum()
#     else:
#         # ## this block will be executed if there is no exception
#         # print(grade)
#         # print("No exception happened")
#         return grade
#
#
# s = askfornum()
# print(s)
##############################################
# grade = input("please enter your grade ")
# try:
#     grade = int(grade)
# except Exception as e:
#     print(e)
#     grade = None
# else:
#     # ## this block will be executed if there is no exception
#     print(grade)
#     print("No exception happened")
# finally:
#     print('this block will be executed always if there is an exception or not')
#     print('-----------------The End------------------------')
# #################### Raising the exception ############################################
def divmums():
    num1= input("please enter num1")
    num2 = input("please enter num2 ")

    if num2=="0":
        raise ZeroDivisionError("Division by zero is not allowed ")

    def validateint(varname):
        if varname.isdigit():
            return int(varname)
        return None

    num1 =validateint(num1)
    num2 = validateint(num2)

    if num1 and num2:
        return num1 /num2
    return None


s = divmums()
print(s)









