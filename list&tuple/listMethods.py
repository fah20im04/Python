list = [1, 2, 3, 4, 5]

#append add element at the end
print(list.append(6))  # None
print(list)  # [1, 2, 3, 4, 5, 6]   

#extend adds multiple elements at the end
list.extend([7, 8])
print(list)  # [1, 2, 3, 4, 5, 6, 7, 8]

#insert adds element at specific index
list.insert(0, 0)   # Insert 0 at index 0   
print(list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8]

#remove deletes specific element
list.remove(4)  # Remove first occurrence of 4  
print(list)  # [0, 1, 2, 3, 5, 6, 7, 8]

#pop removes element at specific index, if no index is provided, it removes the last element
popped_element = list.pop()  # Remove and return last element
print(popped_element)  # 8

print(list)  # [0, 1, 2, 3, 5, 6, 7]

#index returns the index of first occurrence of the element
index_of_5 = list.index(5)  # Get index of first occurrence of 5
print(index_of_5)  # 4

#count returns the number of occurrences of the element
count_of_2 = list.count(2)  # Count occurrences of 2
print(count_of_2)  # 1

#sort sorts the list in ascending order
list.sort()  # Sort the list in ascending order
print(list)  # [0, 1, 2, 3, 5, 6, 7]

#reverse reverses the list
list.reverse()  # Reverse the list  
print(list)  # [7, 6, 5, 3, 2, 1, 0]
print(list.sort(reverse=True))  # None
print(list)  # [7, 6, 5, 3, 2, 1, 0]

#copy creates a shallow copy of the list
copied_list = list.copy()  # Create a shallow copy of the list
print(copied_list)  # [7, 6, 5, 3, 2, 1, 0]

#clear removes all elements from the list
list.clear()  # Remove all elements from the list
print(list)  # []

print(copied_list)  # [7, 6, 5, 3, 2, 1, 0]
