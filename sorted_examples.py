"""
EXPLANATION OF sorted() METHOD IN PYTHON

sorted() is a built-in function that returns a NEW sorted list from an iterable.
It does NOT modify the original list (unlike list.sort() which modifies in-place).

Syntax:
    sorted(iterable, key=None, reverse=False)

Parameters:
    - iterable: The sequence to sort (list, tuple, string, etc.)
    - key: Optional function to determine sorting order
    - reverse: If True, sorts in descending order (default: False)

Returns: A new sorted list
"""

print("=" * 60)
print("BASIC USAGE - Sorting Numbers")
print("=" * 60)

# Example 1: Basic sorting of numbers
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_numbers = sorted(numbers)
print(f"Original: {numbers}")
print(f"Sorted:   {sorted_numbers}")
print(f"Original unchanged: {numbers}")  # Original list is NOT modified
print()

# Example 2: Sorting in reverse order
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
sorted_desc = sorted(numbers, reverse=True)
print(f"Original: {numbers}")
print(f"Descending: {sorted_desc}")
print()

# Example 3: Sorting strings
words = ["banana", "apple", "cherry", "date"]
sorted_words = sorted(words)
print(f"Original: {words}")
print(f"Sorted:   {sorted_words}")
print()

print("=" * 60)
print("USING key PARAMETER - Custom Sorting")
print("=" * 60)

# Example 4: Sorting by length of strings
words = ["apple", "pie", "banana", "a"]
sorted_by_length = sorted(words, key=len)
print(f"Original: {words}")
print(f"Sorted by length: {sorted_by_length}")
print()

# Example 5: Sorting dictionaries by a specific key
students = [
    {'name': 'Alice', 'age': 20, 'grade': 85},
    {'name': 'Bob', 'age': 19, 'grade': 92},
    {'name': 'Charlie', 'age': 21, 'grade': 78}
]

# Sort by age
sorted_by_age = sorted(students, key=lambda x: x['age'])
print("Students sorted by age:")
for student in sorted_by_age:
    print(f"  {student['name']}: age {student['age']}")
print()

# Sort by grade (descending)
sorted_by_grade = sorted(students, key=lambda x: x['grade'], reverse=True)
print("Students sorted by grade (highest first):")
for student in sorted_by_grade:
    print(f"  {student['name']}: grade {student['grade']}")
print()

# Example 6: Sorting by multiple criteria
# First by grade (descending), then by name (ascending)
sorted_multi = sorted(students, key=lambda x: (-x['grade'], x['name']))
print("Students sorted by grade (desc), then name (asc):")
for student in sorted_multi:
    print(f"  {student['name']}: grade {student['grade']}")
print()

print("=" * 60)
print("YOUR TASK MANAGER EXAMPLE")
print("=" * 60)

# Simulating your task manager scenario
tasks = [
    {'id': 1, 'title': 'Task A', 'completed': False},
    {'id': 2, 'title': 'Task B', 'completed': True},
    {'id': 3, 'title': 'Task C', 'completed': False},
    {'id': 4, 'title': 'Task D', 'completed': True},
]

print("Original tasks:")
for task in tasks:
    status = "✓" if task['completed'] else "✗"
    print(f"  {status} {task['title']}")
print()

# Your code: sorted(tasks, key=lambda x: x['completed'], reverse=True)
# This sorts by the 'completed' field
# reverse=True means True values come first (completed tasks first)

sorted_tasks = sorted(tasks, key=lambda x: x['completed'], reverse=True)
print("Sorted tasks (completed first):")
for task in sorted_tasks:
    status = "✓" if task['completed'] else "✗"
    print(f"  {status} {task['title']}")
print()

# Alternative: Sort with False first (incomplete tasks first)
sorted_tasks_incomplete_first = sorted(tasks, key=lambda x: x['completed'])
print("Sorted tasks (incomplete first):")
for task in sorted_tasks_incomplete_first:
    status = "✓" if task['completed'] else "✗"
    print(f"  {status} {task['title']}")
print()

print("=" * 60)
print("ADVANCED EXAMPLES")
print("=" * 60)

# Example 7: Using a named function instead of lambda
def get_grade(student):
    return student['grade']

sorted_by_function = sorted(students, key=get_grade, reverse=True)
print("Using named function as key:")
for student in sorted_by_function:
    print(f"  {student['name']}: {student['grade']}")
print()

# Example 8: Sorting tuples
pairs = [(3, 'c'), (1, 'a'), (2, 'b')]
sorted_pairs = sorted(pairs)  # Sorts by first element, then second
print(f"Tuples: {pairs}")
print(f"Sorted: {sorted_pairs}")
print()

# Example 9: Sorting with case-insensitive string comparison
names = ["Alice", "bob", "Charlie", "david"]
sorted_case_insensitive = sorted(names, key=str.lower)
print(f"Original: {names}")
print(f"Case-insensitive: {sorted_case_insensitive}")
print()

# Example 10: Sorting by absolute value
numbers = [-5, 3, -1, 4, -2]
sorted_abs = sorted(numbers, key=abs)
print(f"Original: {numbers}")
print(f"Sorted by absolute value: {sorted_abs}")
print()

print("=" * 60)
print("KEY DIFFERENCES: sorted() vs list.sort()")
print("=" * 60)

# sorted() returns a new list
original = [3, 1, 2]
new_list = sorted(original)
print(f"Original: {original}")
print(f"New list: {new_list}")
print(f"Are they the same object? {original is new_list}")  # False
print()

# list.sort() modifies the original list
original2 = [3, 1, 2]
original2.sort()
print(f"After .sort(): {original2}")
print(f"Original list was modified!")
print()

print("=" * 60)
print("SUMMARY")
print("=" * 60)
print("""
Key Points:
1. sorted() returns a NEW sorted list (doesn't modify original)
2. key parameter: function to extract comparison value
3. reverse=True: sort in descending order
4. Works with any iterable (lists, tuples, strings, etc.)
5. Lambda functions are commonly used for key parameter

Your code: sorted(tasks, key=lambda x: x['completed'], reverse=True)
- Sorts tasks by the 'completed' field
- reverse=True puts True (completed) tasks first
- Returns a new list, original 'tasks' list unchanged
""")

