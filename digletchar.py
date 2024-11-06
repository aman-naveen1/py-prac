def digit_to_text(digit):
    """Convert a numeric digit to its text representation."""
    digit_names = {
        '0': 'zero',
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine'
    }
    return digit_names.get(digit, "unknown")

def check_character(char):
    """Check if the character is numeric, letter, or special character."""
    if char.isdigit():
        return "numeric", digit_to_text(char)
    elif char.isalpha():
        if char.isupper():
            return "letter", "uppercase"
        else:
            return "letter", "lowercase"
    else:
        return "special character", None

if __name__ == "__main__":
    char = input("Enter a character: ")

    if len(char) != 1:
        print("Please enter exactly one character.")
    else:
        char_type, additional_info = check_character(char)
        print(f"The character '{char}' is a {char_type}.")
        
        if char_type == "letter":
            print(f"It is {additional_info}.")
        elif char_type == "numeric":
            print(f"It is the digit '{char}', which is '{additional_info}' in text.")
