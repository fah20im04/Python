tup = (2, 3, 4, 5)
print(tup.index(4))  # Get index of first occurrence of 4
print(tup.count(3))  # Count occurrences of 3
print(tup)  # (2, 3, 4, 5)

#practice
grade = ("C", "D", "A", "A", "B", "B", "A")
print("Student with grade A:", grade.count("A"))  # 3

grade_list = list(grade)
grade_list.sort()
print (grade_list)  # ['A', 'A', 'A', 'B', 'B', 'C', 'D']