####
############ read , write , append


#read file content


######### write
"""
    overwrite the existing content ---
    write in the file starting from the first byte

"""


# ## append:

"""
    add data at the end of the file 
"""
###########################READ from file#########################
# 1- open the file
# mode be ---> r ---> read , w-> write , a --> append

fileobject = open("mycv.txt", "r")
# print(fileobject)
### do the operation

filedata = fileobject.read()   # read all the file content into one string
print(filedata)  ###
# print(type(filedata))

# 3- close file
fileobject.close()
















