# TUPLES
tpl = 10, 20, 30, 40, 50, "One"
print(tpl)  # (10, 20, 30, 40, 50, 'One')
print(type(tpl))  # <class 'tuple'>

# Console:
tpl1 = (10, 20, 30, 40, 50, 'One')
print(tpl1) # (10, 20, 30, 40, 50, 'One')

# with parameters or without parameters it considers the tuple 

# Use comma if you are using single value/ or else it treats as...
# INT, TUPLE 
tpl = 20
print(type(tpl))  # <class 'int'>

tpl = 20,
print(type(tpl))  # <class 'tuple'>


# STRING, TUPLE
tpl = "one"   
print(type(tpl))  # <class 'str'>

tpl = "one",
print(type(tpl))  # <class 'tuple'>


# SLICING CONCEPTS
tpl = 10, 20, 30, 40, 50, 60, 70

print(tpl)  # (10, 20, 30, 40, 50, 60, 70)

print(tpl[ : ]) # (10, 20, 30, 40, 50, 60, 70)

print(tpl[3:6])  # (40, 50, 60)

print(tpl[3:])  # (40, 50, 60, 70)


# TYPE CONVERSION
x = list((1, 2, 3, 4, 5))  # tuple data in list
print(x)  # [1, 2, 3, 4, 5]

x = tuple([1, 2, 3, 4, 5]) # list data in tuple
print(x)  # (1, 2, 3, 4, 5)


# BREAK STRING
x = list("Hello")  # []
print(x)  # ['H', 'e', 'l', 'l', 'o']

y = tuple("World") # ()
print(y)  # ('W', 'o', 'r', 'l', 'd')


# CREATING COPY OF TUPLES
tpl2 = ( 0, 2, "a", "b")
print(tpl2)  # (0, 2, 'a', 'b')
print(tpl2[:])  # (0, 2, 'a', 'b')
print(tpl2*1)  # (0, 2, 'a', 'b')
print(tpl2 + ())  # (0, 2, 'a', 'b')


# CONCATENATION
tpl3 = (1, 2, 3, 4)
print (tpl3)
print(tpl3 + (5, 6))

print("username", "password") # username password
print("username", + 100) # username 100
print('username', + 20 + 30, + 10) # username 50 10
print('username', + 20 + 30, + 10, "password") # username 50 10 password


# TUPLE REPITATION
t1 = (1, 2, 3, 4, 5)
t2 = (1, 2, 3, 4, 5)
print(t1*2)  # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
print(t1*3)  # (1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)