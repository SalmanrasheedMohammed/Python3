# l1 = []
# print(dir(l1))

# l1 = [10,20,30,40,50]
# print(l1.__iter__())

# r1 = iter(l1)
# print(r1)

# #public
# n1 = next(r1)
# print(n1)
# n1 = next(r1)
# print(n1)
# n1 = next(r1)
# print(n1)
# n1 = next(r1)
# print(n1)
# n1 = next(r1)
# print(n1)
# n1 = next(r1)
# print(n1)

# private
# l1=[10,20,30,40,50]
# print(l1.__iter__())

# r1=l1.__iter__()
# print(r1.__next__())
# print(r1.__next__())
# print(r1.__next__())
# print(r1.__next__())
# print(r1.__next__())

# l1=[10,20,30,40,50]
# res=iter(l1)

# while True:
#     try:
#         element=next(res)
#         print(element)
#     except StopIteration as e:
#         print(e)
#         break
        





# TASK

def even_or_odd(num):
    if num & 1 == 0:
        return "Even"
    else:
        return "Odd"
    
print(even_or_odd(2))
print(even_or_odd(3))
print(even_or_odd(0))



def even_or_odd(num):
    if num & 1 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))

result = even_or_odd(num)

print(f"The number {num} is {result}.")
 