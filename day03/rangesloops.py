
# m = range(5)  ## start =0 , end = 5 ---> range 0,1,2,3,4
# print(m)  # range object ---> (0 ,5) , itertable
#
# for i in m:
#     print(i)

##############
# n = range(1, 10) # start 1 , -----> 9
# for i in n:
#     print(i)


# n = range(1, 10, 2)# start 1 , ----->end 9  with step 2
# for i in n:
#     print(i)

# s = range(1,-1, -1) # 1 , 0 ,
# print(s)
# for i in s:
#     print(i)


# n = range(10, 0, -1)
# for i in n:
#     print(i)


# m= 10
#
# r = range(0, m)  # you make sure that the type of m is int ---> function accept the variable name, type
# # ("noha", str)
# # ("noha", int)
# for i in r:
#     print(i)
################################################ loops

"""
while condition:
    do something
"""

######### ask user to enter his age ---> numeric

# age = input("please enter your age ")
# if age.isdigit():
#     age= int(age)
# else:
#     print("please provide suitable value ")
############### while ---> I don't know the actual number of times.
# age = input("please enter your age ")
# while not age.isdigit():
#     age = input("please enter your age ")
#
# age = int(age)


################## loop statements
# while True:
#     age = input("please enter your age ")
#     if age.isdigit():
#         break  # break the loop
#
# age =int(age)


##########3 NEVER TRUST USER INPUT



# for i in range(5):
#     if i==3:
#         break  #skip iteration
#     print(i)
# else:
#     # this code will be executed if the loop is completeted
#     print("Completed")
# # print("after the loop ")

########################################## Pass
"""
    if(x>0){
    
    }
    for(i=0;i<5;i++){
    }

"""

x= 10

# if x >0:   # test development
#     pass

print("hiiii")

for i in range(10):
    pass  # some logic will be added later

print("byeeeeeeeeeeeee")



