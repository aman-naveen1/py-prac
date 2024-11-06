def main():
    input_string = input("Enter a string: ")

    # Find frequency of a character
    char_to_find = input("Enter a character to find its frequency: ")
    freq = input_string.count(char_to_find)
    print(f"The frequency of '{char_to_find}' in the string is: {freq}")

    # Replace a character
    old_char = input("Enter a character to replace: ")
    new_char = input("Enter the new character: ")
    replaced_string = input_string.replace(old_char, new_char)
    print(f"String after replacing '{old_char}' with '{new_char}': {replaced_string}")

    # Remove first occurrence
    char_to_remove_first = input("Enter a character to remove its first occurrence: ")
    first_removed_string = input_string.replace(char_to_remove_first, '', 1)
    print(f"String after removing the first occurrence of '{char_to_remove_first}': {first_removed_string}")

    # Remove all occurrences
    char_to_remove_all = input("Enter a character to remove all occurrences: ")
    all_removed_string = input_string.replace(char_to_remove_all, '')
    print(f"String after removing all occurrences of '{char_to_remove_all}': {all_removed_string}")

if __name__ == "__main__":
    main()
