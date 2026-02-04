def len_list(list):
    print(len(list))

cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
len_list(cities)

# def print_list(list):
#     for item in list:
#         print(item,end=", ")

# print_list(cities)

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *=i
    print (fact)
factorial(6)

