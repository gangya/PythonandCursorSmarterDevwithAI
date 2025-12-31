#1. Ask the userfor two numbers.
#2. Ask the user for the operation to be executed
#3. The program exution will finish  tilluser tyes exit

def start_calculator():
    while True:
        try:
            number1 = float(input("Enter the first number: "))
            number2 = float(input("Enter the second number: "))
            operation = input("Enter the operation to be executed:\n"
                              "  + : addition\n"
                              "  - : subtraction\n"
                              "  * : multiplication\n"
                              "  / : division\n"
                              "Or type 'exit' to quit: ")
            if operation == "exit":
                    break
            elif operation == "+":
                print(f"The result of {number1} + {number2} is {number1 + number2}")
            elif operation == "-":
                print(f"The result of {number1} - {number2} is {number1 - number2}")
            elif operation == "*":
                print(f"The result of {number1} * {number2} is {number1 * number2}")
            elif operation == "/":
                print(f"The result of {number1} / {number2} is {number1 / number2}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed")
        except ValueError:
            print("Error: Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"An error occurred: {e} in start_calculator function")
    print("Thank you for using the calculator. Goodbye!")

if __name__ == "__main__":
    start_calculator()