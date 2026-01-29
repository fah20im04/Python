#dictionaries are mutable   
info = {
    "key" : "value",
    "name" : "Fahim",
    "learning" : "Python",
    "age" : 25,
    "isAdult": True,
    "marks" : [85, 90, 78, 92],
    "subjects" : ("Math", "Science", "English")
}

info["name"] = "MyLove"  # Modifying an existing value
info["Surname"] = "Ahmed"  # Adding a new key-value pair

"""print(info)  # Output: MyLove
print (type(info))"""

null_dict = {}  # Empty dictionary
null_dict["name"] = "Fahim"
print(null_dict)