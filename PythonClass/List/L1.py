# LISTS(INDEX,LENGTH,COUNT,NESTED,LEN(STR))

# LIST

l = [1,2,3,4,5,10.0,50j, True, False, 50.0]

print(l) # [1, 2, 3, 4, 5, 10.0, 50j, True, False, 50.0]

# list contains (int,float,str,bool,complex)

# index position of the list elements

print(l[2]) # 3
print(l[5]) # 10.0

print(l.index(10.0)) # 5

# len of list elements

print(len(l)) # 10

# count of list elements

print(l.count(10.0)) # 1

# nested list element

ln = [1,2,3,[5,6,7],8,9,10]
print(ln[3]) # [5, 6, 7]
print(ln[2]) # 3

# length of string

li = "Hello Python"
print(len(li)) # 12

# list of id elements

print(id(l[0]), id(l[3])) # 140724914742056 140724914742152