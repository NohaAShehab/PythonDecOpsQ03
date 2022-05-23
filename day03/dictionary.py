# d = {}
#
# print(type(d))
# from python 3.7 dic elements are sorted in memory
info = {"name": "Noha", "email": "nshehab@iti.gov.eg"}

info["track"] = "devops"  # assign key to a value in the dic, key exists before --> update dic , else ,, add it

print(len(info))

######## get keys of dic

# print(info.keys())  # data structure ---> dict_keys ---> can be casted to list or tuple

################ get the values of the dic
# print(info.values())   # dict_values  --> can be casted to list or tuple
#####################
#
# for i in info:   # i represent the key
#     print(i)  # print the key


# for i in info:   # key
#     # print(i, info[i])
#     print(f"key= {i}, value = {info[i]}")

# stdname = "noha"
# track = "devops"
# temp = f"My name is {stdname} I am studing at  {track} track"# bind values from existing variables to the string
# print(temp)

# get index for the items
# for i , v in enumerate(info):   # ignore the values ---> count the key
#     print(f"{i}=>{v}: {info[v]}")


################3
# print(info.items())  # dict_items ---> can be casted to list ---> list of tuples ,,, each tuple --> key, value
#
# for key, value in info.items():
#     print(f"{key}: {value}")

############################
print(info)

### operation --->
# remove item from the dict
res = info.pop("email")  # accept key
print(res)  # hold the value of the dic
print(info)

##############
info["year"] = 2022
info["name"] = "NohaShehab"
print(len(info))
info["courses"] = ["linux", "PHP", "Python", "Mongo"]
##########################
# city_info = {"gov":"Cairo", "city":"October", "street":1, "year":2023}
#
# info.update(city_info)  # update info dic with city_info ---> if key not exists --> add it  ,
# # else --> update existing value

###################################### check the existance

# if "noha" in info:  # check the keys
#     print("hi")
# else:
#     print("byeee")

# if "NohaShehab" in info.values():  # check the keys
#     print("hi")
# else:
#     print("byeee")

# info.clear ---> remove the key-pairs from the dictionary

# del info ---> remove the dictionary form the memory

# del info["name"] # delete the pair from the dictionary

################################### del

del info["name"]  # doesn't allow return assignment

myt = (4,5,6)
del myt
# if you care about the value of the key removed ---> pop
m = info.pop("track")
print(m)