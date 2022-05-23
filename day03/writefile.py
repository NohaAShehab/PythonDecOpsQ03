
# 1- open the file

fileobject = open("info.txt", "w") #write mode

"""
if the file exists 
    write mode --> open file for writing starting from the first byte in file
    ########## remove old content in the file 
if the file not exists===> 
    if the permission on the directory allow it , python will create empty file

"""
# print(fileobject)
###############
# 2- write in the file

# fileobject.write("We neeed the break .......\n")
# fileobject.write("We neeed the break .......\n")
# fileobject.write("We neeed the break .......\n")
fileobject.write("""My name is Noha, 
Python is interesting
Hope you enjoy the course""")


fileobject.close()

################################
"""
    word = "note"
    userinput = ["-","-","-","-"]
    please guess the word (----)
    for i in range(7):
        c = input("please enter char .. ")
        if c in word: 
            ##assue 
            userinput == ["n","-","-","e"]
            
             



"""


"""

    abdcedefghijklmnopqrstuvwxyz
    
    no   2
    h
    as
    h
    eh
    ab
    
    abdu
    lr
    ahm
    an

"""