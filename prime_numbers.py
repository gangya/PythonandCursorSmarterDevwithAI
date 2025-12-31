def start_prime_number():
    number = int(input("Enter a number: "))
    print(prime_number(number))
    assert prime_number(13) == "13 is a prime number"
    assert prime_number(10) == "10 is not a prime number"
    
def prime_number(number):
    """
    Determines if a number is prime.

    Args:
        number (int): The number to check.

    Returns:
        str: A message stating whether the number is prime or not.

    How can I test this function?
    ------------------------------------------
    You can test this function directly in a Python shell or by calling it in your code. Here are some tests:

    >>> print(prime_number(7))
    7 is a prime number

    >>> print(prime_number(12))
    12 is not a prime number

    >>> print(prime_number(2))
    2 is a prime number

    Or, write a few assert statements for automated testing:
    >>> assert prime_number(13) == "13 is a prime number"
    >>> assert prime_number(10) == "10 is not a prime number"
    """
    if number == 2:
        return f"{number} is a prime number"
    for i in range(2, number):
        #print(f"{i} in for ")
        if number % i == 0:
            return f"{number} is not a prime number"
    return f"{number} is a prime number"
        
if __name__ == "__main__":
    start_prime_number()    
    