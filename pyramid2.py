def print_pyramid(rows):
    for i in range(rows):
        print(' ' * (rows - i - 1) + '* ' * (i + 1))

def print_reverse_pyramid(rows):
    for i in range(rows, 0, -1):
        print(' ' * (rows - i) + '* ' * i)

if __name__ == "__main__":
    n = int(input("Enter the number of rows for the pyramids: "))
    
    print("\nPyramid of '*' characters:")
    print_pyramid(n)
    
    print("\nReverse Pyramid of '*' characters:")
    print_reverse_pyramid(n)
