# is used to store key value pair in pyhton. they are undorder and mutable and dont't allow create duplicate keys
# info = {
#     "key" : "value", "name" : "krish.com", "learning" : "python"   
# }
# print(info)

# n dict we can use list or tuple - 
# key m list wgra nhi
# info = {
#     "name" : "krish",
#     "sub" : ["python" , "c++" , "java"] ,"sub1" : ("py" , "c++" , "java")
# }
# print(info)

# accssing of dict - 
# print(info["name"])

# change - 
# a = info["key"] = "marks"
# print(info)

# Nested dict - 
student = {
    "name" : "Ishita",
    "sub" : {
        "phy" : 57, "ch" : 56 , "Hindi" : 45 , "eng" : 89
    }
}
# print(student["name"])


# Methods of dict - 
# print(student.keys())
# if i want that keys in list or tuple form then - 
# print(list(student.keys())) 

# print(student.values())
# print(list(student.values())) # we will get it dict in list form

# print(student.items()) # all dict return 

# print("before")
# print(student["name"]) # it gives an error
# print("after")
# print("before")
# print(student.get("name2")) # it won't give error it gives None
# print("after")

# student.update({"name" : "Krishna belwal"})
# print(student)



# practis questions - 
# Qus = {
#     "table" : ["a piece of furniture" , "list of facts & figures"],
#     "cat" : "a small animal"
# }
# print(Qus)





