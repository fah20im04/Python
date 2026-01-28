tup = (2, 3, 4, 5)
print (tup, "\n", type(tup))
print (tup[2])  # Accessing element at index 2
#tup[1] = 6  # Modifying element at index 1 (This will raise an error)

notTup = (4)
print(notTup, "\n", type(notTup))
tup1 = ()
print(tup1, "\n", type(tup1))
tup2 = (5,)
print(tup2, "\n", type(tup2))

print(tup + tup2)  # Concatenation
print(tup * 2)     # Repetition
print(tup[1:4])   # Slicing
print(tup[::-1])  # Reversing