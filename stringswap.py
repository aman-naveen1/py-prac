# Get input from the user
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")
n = int(input("Enter the number of characters to swap: "))

# Check if n is valid
if n > len(str1) or n > len(str2):
    print("Error: n is greater than the length of one or both strings.")
else:
    # Swap the first n characters
    new_str1 = str2[:n] + str1[n:]
    new_str2 = str1[:n] + str2[n:]

    # Print the swapped strings
    print("String 1 after swapping:", new_str1)
    print("String 2 after swapping:", new_str2)
