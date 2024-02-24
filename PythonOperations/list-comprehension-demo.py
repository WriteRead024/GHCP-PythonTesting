
# Feb. 23 2024
# GitHub CoPilot
# with Rich W.
# MSL.l

print()
print("demo of list comprehension operation")
print()
print("list comprehension is a way to create a new list from an existing list")
print("without explicitly writing the list elements individually")
print()

# Original list
numbers = [1, 2, 3, 4, 5]

# List comprehension to create a new list with squared values
squared_numbers = [x**2 for x in numbers]

print()
print("list comprehension operation: squared_numbers = [x**2 for x in numbers]")
print()

# Print the original list and the squared list
print("Original list:", numbers)
print("Squared list:", squared_numbers)