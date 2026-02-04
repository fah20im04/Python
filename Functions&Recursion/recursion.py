def show(n):
    if(n==6):
        return
    print(n)
    show(n+1)
# show(5)

def fact(n):
    if n == 0 or n==1:
        return 1
    else:
        return n * fact(n-1)

# print (fact(5))

movies = ["Inception", "The Dark Knight", "Interstellar", "Parasite", "Avengers: Endgame"]  

def print_list(list, idx):
    if(idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
print_list(movies,0)

# def elementInList(list):
#     if(len(list)==0):
#         return
#     else:
#         print(list[0])
#         elementInList(list[1:])

# elementInList(movies)
