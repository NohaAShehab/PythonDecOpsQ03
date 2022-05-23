
def register():
    firstname = input("please enter firstname ")
    email= input("please enter your email ")
    password  = input("please enter your password")
    user_data = f"{firstname}:{email}:{password}\n"
    usersfile= open("users.txt","a")
    ### prepare data
    usersfile.write(user_data)
    usersfile.close()

def getallusers():
    usersfile = open("users.txt", "r")
    usersdata = usersfile.readlines()  #read file content into a list
    for i in usersdata:
        i = i.strip("\n")  # remove chars from the beginning and the end of the string
        user = i.split(":")  # split string into parts ---> according to seperator
        # save content into a list
        print(user)
    # print(usersdata)
    usersfile.close()

getallusers()


# register()



