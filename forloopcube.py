def cubes_of_even_numbers_for_loop(input_list):
    """Returns a list of cubes of even integers from the input list using a for loop."""
    cubes = []
    for num in input_list:
        if num % 2 == 0:  # Check if the number is even
            cubes.append(num ** 3)  # Append the cube of the even number
    return cubes

# Example usage
if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = cubes_of_even_numbers_for_loop(input_list)
    print("Cubes of even integers (for loop):", result)
