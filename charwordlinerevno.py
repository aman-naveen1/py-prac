def analyze_file(file_path):
    """Analyze the specified file for character count, word count, line count, character frequency, and reversed words."""
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            
            # Count total characters
            total_characters = len(content)
            
            # Count total words
            words = content.split()
            total_words = len(words)
            
            # Count total lines
            total_lines = content.count('\n') + 1
            
            # Calculate frequency of each character
            char_frequency = {}
            for char in content:
                char_frequency[char] = char_frequency.get(char, 0) + 1
            
            # Print results
            print(f"Total Characters: {total_characters}")
            print(f"Total Words: {total_words}")
            print(f"Total Lines: {total_lines}")
            print("Character Frequency:", char_frequency)
            print("Words in Reverse Order:", " ".join(reversed(words)))

    except FileNotFoundError:
        print("The specified file was not found.")

# Example usage
if __name__ == "__main__":
    file_path = input("Enter the path of the file to analyze: ")
    analyze_file(file_path)
