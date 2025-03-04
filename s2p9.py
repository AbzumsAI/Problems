# session 2
# functions
# problem num. 9

def f(n):
    if n % 2 == 0:
        return n // 2  # Even case
    else:
        return (1 - n) // 2  # Odd case

def is_one_to_one():
    # Create a dictionary to store outputs and their corresponding inputs
    output_dict = {}

    # Test for a reasonable range of natural numbers (e.g., 1 to 1000)
    for n in range(1, 1001):
        result = f(n)
        if result in output_dict:
            # If the output is already in the dictionary, the function is not one-to-one
            print(f"The function is not one-to-one because f({n}) = f({output_dict[result]}) = {result}")
            return False
        else:
            # Store the output and its corresponding input
            output_dict[result] = n

    # If no duplicates are found, the function is one-to-one
    print("The function is one-to-one.")
    return True

# Check if the function is one-to-one
is_one_to_one()