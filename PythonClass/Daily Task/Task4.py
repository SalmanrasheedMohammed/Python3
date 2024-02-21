def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)

# Get user input
num = int(input("Enter a number: "))

# Call the function with the user input
result = factorial(num)

# Print the result
print(f"The factorial of {num} is {result}.")
