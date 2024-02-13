# Define a dictionary with key-value pairs
dict = {'apple': 3, 'banana': 5, 'orange': 2}


# Accessing values using keys
print(dict['apple'])  # Output: 3
print(dict['orange'])  # Output: 2


# Adding a new key-value pair
dict['grape'] = 4
print(dict)  # Output: {'apple': 3, 'banana': 5, 'orange': 2, 'grape': 4}


# Modifying the value associated with a key
dict['banana'] = 6
print(dict)  # Output: {'apple': 3, 'banana': 6, 'orange': 2, 'grape': 4}


# Removing a key-value pair
del dict['orange']
print(dict)  # Output: {'apple': 3, 'banana': 6, 'grape': 4}


# Check if a key exists
print('apple' in dict)  # Output: True


# Iterate over keys
for key in dict:
    print(key, dict[key])

# Output:
""""
apple 3
banana 6
grape 4

"""