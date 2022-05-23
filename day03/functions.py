# ################ functions with known number of arguments ##########

# def getfullname(firsname, lastname):
#     fullname = f"{firsname} {lastname}"
#     print(fullname)
#     return
#
#
# s=getfullname("noha","Shehab")
# print(s)   # return with None ---> falsy values
#
# getfullname("Ahmed","Mohamed")

#########################################
# def addnums(x :int, y:int):  # for developer
#     sum = x  + y
#     print(sum)
#     return sum


# addnums(10)
# s=addnums(10, 15)
# print(s)   # return with None ---> falsy values
# m = addnums("Ahmed", "Ali")
# # n=addnums("Ahmed",10)

# ##############################  default arguments
# #############3 non-default arguments shouldn't preceeds default arguments
# def mulnums(num1=10, num2=10):
#     print(f"num1= {num1}, num2 = {num2}")
#     res = num1 * num2
#     return res
#
#
# s =mulnums(10, 20)
# print(s)
#
# mres = mulnums(2)
# print(mres)
#
# m = mulnums(5)
# print(m)

# ###################### I don't know the number of arguments.


# def sumnums(*nums):
#     print(type(nums)) ### tuple
#     print(nums)
#     res = 0
#     for i in nums:
#         print(i)
#         res+= i
#
#     print(f"sum= {res}")
#     print("--------------------------------")
#
#
# sumnums()
# sumnums(4,5,5,6)
#
#
# sumnums(10,20)
#
#
# sumnums(300, 4000, 44)
# ######################### unknown number of arguments or key ###############################

def askforinfo(**info):
    print(info)  # dictionary




askforinfo(name="noha",works_at='iti',age=30)

askforinfo(firstname="Omar",lives_at="cairo")

askforinfo()







