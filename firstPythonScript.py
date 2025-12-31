print("hello world!")

# This loop prints the numbers from 0 to 9, separated by spaces.
for i in range(10):
    print(i, end=" ")
    
print("\n")

# Calculate the factorial of a given number

def factorial(n):
    """
    Calculate the factorial of a non-negative integer n using recursion.

    Parameters:
        n (int): A non-negative integer whose factorial is to be computed.

    Returns:
        int: The factorial of the input integer n.

    Raises:
        RecursionError: If the recursion limit is exceeded.
        ValueError: If n is negative or not an integer.

        Example:
            >>> factorial(-1)
            Traceback (most recent call last):
                ...
            ValueError: n must be a non-negative integer

        The function raises a ValueError if n is negative or not an integer by evaluating the type and value of n at the start of the function.
    """
    if n == 0 or n == 1:
        return 1
    else:
        if not isinstance(n, int):
            raise ValueError("n must be an integer")
        if n < 0:
            raise ValueError("n must be a non-negative integer")
        return n * factorial(n-1)
    
    
number = int(input("Enter a number: "))
print(f"the factorial of {number} is {factorial(number)}")

print("done!")