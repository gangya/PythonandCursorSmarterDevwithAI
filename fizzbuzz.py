def start_fizzbuzz():
    print("FizzBuzz Game")
    try:
        number = float(input("Enter a number: "))
        check_fizzbuzz(number)
    except ValueError:
        print("Error: Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {e} in start_fizzbuzz function")

def check_fizzbuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        print(f"FizzBuzz {number} is a multiple of 3 and 5")
    elif number % 3 == 0:
        print(f"Fizz {number} is a multiple of 3")
    elif number % 5 == 0:
        print(f"Buzz {number} is a multiple of 5")
    else:
        print(f"The number {number} is not a multiple of 3 or 5")
        
if __name__ == "__main__":
    start_fizzbuzz()