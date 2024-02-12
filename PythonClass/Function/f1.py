# prog 1
def d1():
    
    print("d1 function")
    
    def d2():
        
        print("d2 function")
    return d2

d = d1()
print(d)
print(d.__name__)
d()

# prog 2
def d1(a):
    def d2(b):
        return print(a+b)
    return d2

d = d1(10)
d(20)
