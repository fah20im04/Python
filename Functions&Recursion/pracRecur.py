def numbers(n):
    if n == 0:
        return
    else:
        print(n , end = ' ')
        numbers(n-1)
# numbers(5)
    
def sum(n):
    sm = 0
    if n == 0:
        return 0
    else:
        return n + sum(n-1)
# print("\n",sum(10))

def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
# print(fact(5))

elements = ['a','b','c','d','e','f']

def elem(list,idx):
    if idx < 0 :
        return
    else :
        print(list[idx])
        elem(list,idx-1)
# elem(elements,len(elements)-1)

def withoutLen(list):
    if not list:
        return 0
    else:
        return 1 + withoutLen(list[1:])
# print(withoutLen(elements))

set = [1,2,3]



def subset(set):
   result = []

   def backtrack(index,current):
       if index == len(set):
           result.append(current.copy())
           return
       
       current.append(set[index])
       backtrack(index + 1,current)

       current.pop()

       backtrack(index+1,current)
    
   backtrack(0,[])
   return result
sets = subset(set)
sets.sort()
x = list(sets)

for s in x:
    print(s)


        