""" list is mutable datatype ---> content of the list can be change time"""
#
# names = list(["Ahmed", "Mohamed", "Mostafa"])
# l3 = ["a", 5, "test", True, names]
# # print(l3[2])
#
# # print(l3)
#
# courses = ["python", "Django", "flask"]
# #
# corecourses = ["Devops", "CICD", "GCP", "AWS"]
# #
# # corecourses.extend(courses)
#
# # contactination
#
# allcourses = courses + corecourses
#
# print(allcourses)
#
# ######################## loooooooooooops  ################
#
# no_of_elemets = len(allcourses)
# i = 0
# """
# for(i=0;i<no_of_elements; i++):
#     print(allcourses[i])
# """
#
# # for item in allcourses:
# #     print(item)
#
#
# # enumarate
# """
# ['python', 'Django', 'flask', 'Devops', 'CICD', 'GCP', 'AWS']
# """
# courses_enum = enumerate(allcourses)
# print(courses_enum)  # return with <enumerate object at 0x7fc0f9ca4bc0> ---> can be iterated
# # enumrate - --> create iterator for the itertable
# # for m in enumerate(allcourses):
# #     print(m)
# # for index, item in enumerate(allcourses):  #
# #     print(f"{index} ---> {item}")
#
# ##################
# name = "Noha Shehab"  # string is itertable
# for n in name:
#     print(n)

##################################

t = ("noha", "ahmed", "Asmaa", "sara")  # tuple
print(type(t))
print(len(t))

# names = ("Mohamed", "Mostafa", "Omar")
# students = t + names
#
# for i in students:
#     print(i)
#
#
# print("ahmed" in students)

# myt = ("noha",)  # tuple of one item
# print(type(myt))

myt = tuple(["noha"])
########################### casting between tuple and list
l = [4, "6", "gkljkl", "gdfgd"]
t = tuple(l)

n = tuple([4, "6", "gkljkl", "gdfgd"])

name = "Noha Shehab"
name = f"{name}#"
nn = list(name)
nn.extend((3,4,5,6,7))
nn.extend(["Ahmed"])


