# day = "Sunday"
#
# if day == 'Sunday':
#     print("Wish you a happy week ^^ ")
# elif day == "Thursday":
#     print("Enjoy your weekend")
# else:
#     print("It seems impossible until it is done ;) ")

##############
# work = "Information Technology Institute"
# print(work[2:8])  # retrun substring (start, end-1)
# print(work[-2])
# # print(work[100])  # string index out of range
# print(work.count("i"))

############### string intepolation
# fname = "Noha "
# midname = "Abd El-Hady "
# lname = "Shehab"
#
# # fullname = fname+" "+ midname+ " "+ midname+" "+lname
# fullname = fname  + midname*2 + lname
# print(fullname)


####################
# msg = "we are $ student in the class $ "
# print(msg.replace("$", str(27),1))  # passed parameter must be string.....
#
#
# print(msg.replace("$", "27"))  # passed parameter must be string.....

# num = 27
# print(msg.replace("$", num))  #
#
#

##########################################
# name = "iti"
# # name = int(name)  # runtime error
#
# x = "10"
# # x = int(x)
#
# ############# check the value inside the string
#
# print(x.isdigit())   # english 1,2,3,4, # ### x.isnumeric()  # support different representation
#
# print(name.isalpha())  # check string contains only chars ---> a--z
#
# print(name.isspace())
#
# ##################################### ask user to enter value
#
# email = input("please enter the email ")
# if not email.isspace():  # check all the string is only space
#     print(email)
#     print(len(email))
# else:
#     print("please provide suitable value ")

########### remove spaces from the beginning or the end of the string strip, lstrip, rstrip

# msg = "       Python is easy     "
# print(len(msg))
# newmsg = msg.strip("yas ")  # edges  ,,, accept set of chars
# print(len(newmsg))
# print(msg)
# print(newmsg)
############################################
name = "Noha"
faculty = "Engineering"
# greet = "My name is {0} I graduated from faculty of {1}"
# print(greet.format(name, faculty))
# print(greet.format(faculty, name))
# greet = "My name is {n} I graduated from faculty of {f}"
# print(greet.format(n=name,f=faculty))
# print(greet.format(f=faculty, n=name))

############33333 f-string
grad_year = 2014
happy = True
greet = f"My name is {name} I graduated from faculty of {faculty}, {grad_year}, {happy}"  # return pure string
print(type(greet))
print(greet)

###################
# n = input("please enter value ")  # return with string
# print(type(n))   # use string function
# if n.isdigit():   #### isdigit() --> return true if the value in n is numeric value ---> can be casted soomthly to int
#     n =int(n)

# val = 100
# print(val.isdigit())  # 'int' object has no attribute 'isdigit'

########################## complex  number
# c = 4+5j
# print(type(c))  # complex
#
# m = complex(4, 5)
# print(type(m))


####################################3 string functions
#
# x ="100"
# # print(type(x))
# # # check the value in the string
# print(x.isdigit())
# # print(x.isalpha())
# # print(x.isspace())
#
# year = 2022
# print(year.isdigit())  #'int' object has no attribute 'isdigit'
################################## Numbers functions
x = 1000.5346
print(round(x))

# print(max(7,8,100,99,-1000))
# print(min(7,8,100,"99",-1000))  #min, max ---> based on comparsion ---> > and <
# '<' not supported between instances of 'str' and 'int'

print(min("300", "45", "55"))























