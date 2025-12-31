#TODO: Create a list of squares of the first n natural numbers using a list comprehension.
def squares(n):
    return [i**2 for i in range(1, n+1)]
print(f"The squares of the first 10 natural numbers are: {squares(10)}")

#TODO: Create a function that takes a list of numbers and returns the sum of the squares of the numbers.
def sum_of_squares(numbers):
    return sum(i**2 for i in numbers)

print(f"The sum of the squares of the numbers 1, 2, 3, 4, 5 is: {sum_of_squares([1, 2, 3, 4, 5])}")

#TODO: Create a function that takes a list of numbers and returns the average of the numbers.
def average(numbers):
    return sum(numbers) / len(numbers)

print(f"The average of the numbers 1, 2, 3, 4, 5 is: {average([1, 2, 3, 4, 5])}")

#TODO: Create a function that takes a list of numbers and returns the median of the numbers.

"""
HOW MEDIAN IS CALCULATED:

The median is the middle value of a sorted list. The calculation differs based on list length:

1. ODD LENGTH (e.g., [1, 3, 5, 7, 9] has 5 elements):
   - Sort the list: [1, 3, 5, 7, 9]
   - Find the middle index: len(numbers) // 2 = 5 // 2 = 2
   - Return the value at that index: numbers[2] = 5
   - The median is 5 (the middle value)

2. EVEN LENGTH (e.g., [1, 3, 5, 7] has 4 elements):
   - Sort the list: [1, 3, 5, 7]
   - There are TWO middle values: 3 and 5 (at indices 1 and 2)
   - Calculate the average of these two values: (3 + 5) / 2 = 4.0
   - The median is 4.0 (the average of the two middle values)

General formula:
- If odd: median = sorted_list[len // 2]
- If even: median = (sorted_list[len // 2 - 1] + sorted_list[len // 2]) / 2
"""

def median(numbers):
    if not numbers:
        raise ValueError("Cannot calculate median of an empty list")
    
    sorted_nums = sorted(numbers)
    length = len(sorted_nums)
    
    if length % 2 == 1:  # Odd length
        # Return the middle element
        middle_index = length // 2
        return sorted_nums[middle_index]
    else:  # Even length
        # Return the average of the two middle elements
        upper_middle = length // 2
        lower_middle = upper_middle - 1
        return (sorted_nums[lower_middle] + sorted_nums[upper_middle]) / 2

# Examples demonstrating odd and even length cases
print(f"\n--- Median Examples ---")
print(f"Odd length - [15, 24, 63, 24, 65]: {median([15, 24, 63, 24, 65])}")
print(f"  Sorted: {sorted([15, 24, 63, 24, 65])} -> Middle value: 24")
print(f"\nEven length - [1, 3, 5, 7]: {median([1, 3, 5, 7])}")
print(f"  Sorted: {sorted([1, 3, 5, 7])} -> Average of 3 and 5: (3+5)/2 = 4.0")
print(f"\nEven length - [10, 20, 30, 40, 50, 60]: {median([10, 20, 30, 40, 50, 60])}")
print(f"  Sorted: {sorted([10, 20, 30, 40, 50, 60])} -> Average of 30 and 40: (30+40)/2 = 35.0")

#TODO: Create a function that takes a list of numbers and returns the mode of the numbers.