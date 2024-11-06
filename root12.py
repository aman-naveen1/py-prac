import math

def find_roots(a, b, c):
    if a == 0:
        print("Invalid input: 'a' cannot be zero for a quadratic equation.")
        return

    # Calculate the discriminant
    discriminant = b**2 - 4*a*c
    
    # Check the nature of the roots
    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Roots are real and different:")
        print(f"Root 1: {root1}")
        print(f"Root 2: {root2}")
    elif discriminant == 0:
        # One real root (both roots are the same)
        root = -b / (2 * a)
        print("Roots are real and the same:")
        print(f"Root: {root}")
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        print("Roots are complex:")
        print(f"Root 1: {real_part} + {imaginary_part}i")
        print(f"Root 2: {real_part} - {imaginary_part}i")

if __name__ == "__main__":
    # User input for coefficients
    try:
        a = float(input("Enter coefficient a (non-zero): "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        
        find_roots(a, b, c)
    except ValueError:
        print("Invalid input. Please enter numeric values.")
