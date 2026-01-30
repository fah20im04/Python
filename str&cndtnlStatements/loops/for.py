# for i in range (5):
#     print("Hello World")
#     while i % 2 == 0:
#         print(f"{i} is even")
#         break
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1
# print('loop ended')

# n = int(input("Enter a number: "))
# i =1
# while i <= 10:
#     print (n * i)    
#     i += 1

# numbers = [1,4,9,16,25,36,49,64,81,100]
# # Create a dictionary where each number is a key and its value is a list of its factors
# elements = {}

# for num in numbers:9

#     factors = []
#     for i in range(1, num + 1):
#         if num % i == 0:
#             factors.append(i)
#     elements[num] = factors
# print(elements.values())

numbers = (1,4,9,16,25,36,49,64,81,100)

x = int(input("Enter a number : "))

if x in numbers:
    print(f"{x} is present in the tuple")
else:
    print(f"{x} is not present in the tuple")
        

