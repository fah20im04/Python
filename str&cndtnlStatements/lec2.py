# str1 = "helloWorld"

# print(str1[6:12])  # slicing strings
# print(str1.upper())  # converting to uppercase
# #" this is how apostrophy's work in strings
# print (str1[:-6])  # negative indexing
# print (str1[-6:len(str1)])  # negative indexing with slicing

a = "madam"
if a == a[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


""""a = input("Enter string: ")  # "madam"
mid = len(a) // 2

b = a[mid:]              # "dam"
rev_b = ''.join(reversed(b))  # "mad"

first_half = a[:mid+1]   # "mad"

print(rev_b, "its reversed b")
print(first_half)

if rev_b == first_half:
    print("palindrome")
else:
    print("not palindrome")""""

