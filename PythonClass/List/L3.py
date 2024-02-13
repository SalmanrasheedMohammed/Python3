# INSERT ( it will add the data at the given index)
# insert
list = [1, 2, 3, 4, 5, 6, 7, 8]
list.insert(4, 6)

print(list) # [1, 2, 3, 4, 6, 5, 6, 7, 8]

#remove
list.remove(3)
print(list) # [1, 2, 4, 6, 5, 6, 7, 8]
# list.clear-- to remove all the list items

# copy the list
list.copy()
print(list) # [1, 2, 4, 6, 5, 6, 7, 8]

# add strings in the list
l1 = "hello "
l2 = "world"
print(l1 + l2) 
