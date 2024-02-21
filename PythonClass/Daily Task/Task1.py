# TASK-- Find the Number is Even or Odd
# normal Function
def even_or_odd(num):
    if num & 1 == 0:
        return "Even"
    else:
        return "Odd"
    
print(even_or_odd(2))
print(even_or_odd(3))
print(even_or_odd(0))


# Input function
def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

num = int(input("Enter a number: "))

result = even_or_odd(num)

print(f"The number {num} is {result}.")