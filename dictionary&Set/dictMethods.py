student = {
    "name": "Alice",
    "Subjects": {
        "Math": {
            "marks": 95,
            "grade": "A"
        },
        "Science": {
            "marks": 88,
            "grade": "B+"
        },
        "English": {
            "marks": 92,
            "grade": "A-"
        }
    }
}

#print(student["Subjects"]["Math"]["marks"])  # Output: 95
student["Subjects"]["Science"]["marks"] = 90  # Updating marks for Science
student["Subjects"]["History"] = {
    "marks": 85,
    "grade": "B"
}  # Adding a new subject
#print(student)
# Output: 95

"""print(student.keys())
print(student["Subjects"].keys())
print(student.values())
print(list(student["Subjects"].values()))"""

float_marks = student["Subjects"]["Math"]["marks"] + student["Subjects"]["Science"]["marks"] + student["Subjects"]["English"]["marks"]
average_marks = float_marks / 3
"""
print(average_marks)  # Output: 92.33333333333333
print(list(student.keys()))  # Output: Subjects
print(len(list(student.keys())))  # Output: 2 """

#print(list(student.items()))

pairs = list(student["Subjects"].items())
#print(pairs[0])  # Output: dict_items([...])

#print(student["name"])
#print(student.get("name"))

#print(student["name2"])  # This will raise a KeyError
#print(student.get("name2"))  # This will return None

new_info = {"city": "New York","age": 20}
student.update(new_info)
print(student)

#print(student)
# Output: {'name': 'Alice', 'Subjects': {'Math': {'marks': 95, 'grade': 'A'}, 'Science': {'marks': 90, 'grade': 'B+'}, 'English': {'marks': 92, 'grade': 'A-'}, 'History': {'marks': 85, 'grade': 'B'}}, 'city': 'New York', 'age': 20}
