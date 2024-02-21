# TASK -- Find the largest number of among 3 numbers

def find_largest(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

# Test the function with some numbers
print(find_largest(1, 2, 3))  # Output: 3
print(find_largest(5, 2, 5))  # Output: 5
print(find_largest(10, 8, 6)) # Output: 10


# Input Function
def find_largest(num1, num2, num3):
    return max(num1, num2, num3)

# Get user input for the three numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Call the function with the user input
largest = find_largest(num1, num2, num3)

# Print the largest number
print(f"The largest number is {largest}.")

