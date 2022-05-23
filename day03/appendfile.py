
fileobj = open("info.txt", "a")

"""
if the file exists 
    apped mode --> open file for writing starting from the last line of the file
if the file not exists===> 
    if the permission on the directory allow it , python will create empty file

"""

fileobj.write("Hope you are doing well\n")


fileobj.close()

