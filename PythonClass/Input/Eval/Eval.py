
# eval()
i = input("Enter any type: ")
print(i)
e = eval(i)
print(type(e))

# output
"""
    Enter any type: 10
10
<class 'int'>

Enter any type: 2.0
2.0
<class 'float'>

Enter any type: 10,20,30
10,20,30
<class 'tuple'>

Enter any type: {10,20,30,40}
{10,20,30,40}
<class 'set'>

Enter any type: "rasheed"
"rasheed"
<class 'str'>

"""