things = {
    "table" : ['a piece of furniture', 'used for eating or working'],
    "cat" : "a small animal"
}

# print(things,"\n",type(things))

subjects = {"python", "java", "c++", "javascript","python","java","c++","c", "html"}

# print(len(subjects))

# subjects= {}
# for i in range (3):
#     subKey = input(f"Enter subject {i+1}: ")
#     subValue = input(f"Enter marks for {subKey}: ")
#     subjects[subKey] = subValue
# print(subjects)

# set cant differentiate between 9 and 9.0
values = {9,9.0}
print(values)
# this is how we can store both 9 and 9.0 in set
values.add("9.0")
print(values)

values1 = {("float", 9.0), ("int", 9)}
print(values1)