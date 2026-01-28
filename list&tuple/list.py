"""marks = [85, 90.44, 78.5, 92, 88]
print(marks,"\n",type(marks))
print(marks[2])  # Accessing element at index 2
marks[1] = 95.5  # Modifying element at index 1
print(marks)"""

student = ["Fahim", 21, "Male", True]
print(student,"\n",type(student))
print(student[0])  # Accessing element at index 0

"""#practice
favMovies = []
for i in range (3) :
    movie = input(f"Enter your favorite movie {i+1}: ")
    favMovies.append(movie)
print("Your favorite movies are: ", favMovies) """

#practice2

"""list1 = []
for i in range(5):
    element = input()
    list1.append(element)
list2 = list1.copy()
list2.reverse()
if list1 == list2:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")"""

list1 = []
for i in range(5):
    element = input()
    list1.append(element)

is_palindrome = True
n = len(list1)

for i in range(n // 2):
    if list1[i] != list1[n - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")
