#list and dictionary cant be insert inside set because they are mutable
#but tuple can be inserted inside set because it is immutable

collection ={4,2,3,1,"hello","myLove"}

#print(collection)
#print(type(collection))
#print(len(collection))#total number of elements in set
collection.add("Fahim")#adding new element to set
collection.remove(2)#removing element from set
collection.discard(10)#if element is not found it will not raise any error
collection.pop()#removes a random element from set
#collection.clear()#removes all elements from set



collection1 = set()#empty set
#print(type(collection1))

collection1.add(10)
collection1.add(20) 
#print(collection1)
collection1.add((1,2,3))#adding tuple to set
#print(collection1)
collection1.remove(10)
collection1.discard(30)#no error will be raised
#print(collection1)
collection1.pop()
#print(collection1)

#collection1.clear()
#print(len(collection1))

#print(collection1)
set1 = {1,2,3,4}
set2 = {3,4,5,6}
unionSet = set1.union(set2)
#returns a new set containing all unique elements from both sets

print(unionSet)

intersectionSet = set1.intersection(set2)
#returns a new set containing only elements present in both sets    s
print(intersectionSet)

