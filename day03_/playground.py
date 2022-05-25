############## get part of the module  ##################################
# from arthemiticmodule import addnums
#
# print("------------------------------------------")
# m = addnums(200, 2000)
# print(m)

# # ############# alias for the imported block  ##############
# from arthemiticmodule import addnums as add
# r=add(3,45)
# print(r)

# #################################### import all module #########################################
# import arthemiticmodule
#
# m = arthemiticmodule.addnums(34,5)
# print(m)
#
# n = arthemiticmodule.mulnums(5,6)
# print(n)


# ###################### import block from different package
# from iti.greetingmodule import sayhello
#
# sayhello("noha")

# import iti.greetingmodule  as greet
#
# greet.sayhello("Ahmed")
##########################################
# from devops.validation import askfornum
# from devops import askfornum
#
# s = askfornum("day")
# print(s)


# from test import printpi
# printpi()
# import math
# import test
#
# test.printpi()
#
# print(test.math.pi)

###########################
info = {"name": "noha", "id": 1}

print(f"{info['id']}")
