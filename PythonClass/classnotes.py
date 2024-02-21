# # names = ["admin", "admin", "admin", "not admin", "admin"]
# # l1 = [i if i == "admin" else "not admin there" for i in names]
# # print(l1)


# # names = ["sai", "kiran", "vishnu", "kirshna"]
# # l2 = [i if i == "vishnu" else "not sai" for i in names]
# # print(l2)

# l1 = [x+y for x in [10,20,30] for y in [2,3]]
# print(l1)

# l1 = []
# for i in [5,10,15]:
#     for j in [2]:
#         l1.append(i*j)
# print(l1)
    
# l2 = []
# for i in [5,10,15]:
#     for j in [2]:
#         l2.append(i+j)
# print(l2)


# FEB 20

# def d1():
#     return 10
#     return 20
#     return 30

# d = d1()
# print(d, type(d1))

# def d1():
#     return 10, 20, 30


# d = d1()
# print(d, type(d1))

# def d2():
#     yield 10
#     yield 20
#     yield 30
    
# d = d2()
# print(d)
# print(type(d2))

# print(next(d))
# print(next(d))
# print(next(d))

# def d3():
#     yield 10
#     yield 20
#     return 30
#     yield 40

# d = d3()
# print(next(d))
# print(next(d))
# # print(next(d))

# # generator comprehension
# t1 = ( i for i in range(10))
# print(t1)
# print(tuple(t1))

# TASK1
# l1 = [10,20,30,40,50]
# l = []
# r1 = lambda n : n*2
# for i in l1:
#     l.append(r1(i))
    
# print(l)
# print(l1)

# # map(funct, iterables)
# l1 = [10,20,30,40,50]
# def d1(n):
#     return n*2

# r = map(d1, l1)
# print(r)
# print(list(r))

# print(list(map(lambda n :n*3, [10,20,30,40,50])))

# # TASK2
# l1 = [1,2,3,4]
# l2 = [2,3,4,5]

# def d1(a,b):
#     return a + b

# y = map(d1, l1, l2)
# print(list(y))

# print(list(map(lambda a, b: a + b, l1, l2)))

