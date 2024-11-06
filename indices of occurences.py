def find_occurrences(main_string, sub_string):
    """Returns the starting indices of all occurrences of sub_string in main_string."""
    indices = []
    index = main_string.find(sub_string)  # Find the first occurrence

    # Loop to find all occurrences
    while index != -1:
        indices.append(index)  # Store the index
        index = main_string.find(sub_string, index + 1)  # Find next occurrence

    return indices if indices else -1  # Return indices or -1 if not found

# Example usage
if __name__ == "__main__":
    str1 = input("Enter the main string: ")
    str2 = input("Enter the substring to find: ")
    
    result = find_occurrences(str1, str2)
    print("Indices of occurrences:", result)
