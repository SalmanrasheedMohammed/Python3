# INPUT Data

i = input("Enter your Name: ")
print(i) # Salman Rasheed

# casting
j = int(input("Enter the ID: ")) 
k = int(input("Enter the Phone Number: ")) 
print(j) # 29009
print(k) # 456789123

# list of elements
l = [input("Enter a list of elements: ")]
print(l) # ['10,20,30,40']

# Enter list
l1 = list([input('Enter value a: '), input('Enter value b: ')])
print(l1) # ['10', '20']

# tuple of elements
t = (input("Enter a tuple of elements: "))
print(t) # 10,20,30,40

# enter a dict to tuple
t1 = tuple([input('Enter value a: '), input('Enter value b: ')])
print(t1) # ('10','20')

# set of elements
s = {input("Enter a set of elements: ")}
print(s) # {'10,20,30,40'}

# enter set 
s1 = {input('Enter value a: '), input('Enter value b: ')}
print(s1) # {'10', '20'}

# Dict of elements
d = {
    1 : int(input("Enter a Number: ")),
    2 : float(input("Enter a Float Value: "))
}
print(d) # {1: 56, 2: 5.6}
