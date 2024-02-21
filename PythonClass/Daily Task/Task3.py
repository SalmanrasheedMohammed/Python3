def palindrome(s):

    s = ''.join(c.lower() for c in s if c.isalnum())
    
    return s == s[::-1]

# print(palindrome("olo"))
# print(palindrome("hello"))

string = input("Enter a string: ")

result = palindrome(string)


if result:
    print(f"The string '{string}' is a palindrome.")
else:
    print(f"The string '{string}' is not a palindrome.")