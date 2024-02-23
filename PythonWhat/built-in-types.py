
# Feb. 23, 2024
# Rich W.
# with GitHub CoPilot
# MSL.l

# informed by documentation webpage at:
# https://docs.python.org/3/library/stdtypes.html

print("exploration of built-in Python types")
print()


my_int = 1  # integer
my_float = 1.0  # float
my_bool = True  # boolean
my_string = "string"  # string
my_list = []  # empty list
my_dict = {}  # empty dictionary

# Check the type of my_int
if isinstance(my_int, int):
    print("my_int is of type int")
else:
    print("my_int is NOT of type int")

# Check the type of my_float
if isinstance(my_float, float):
    print("my_float is of type float")
else:
    print("my_float is NOT of type float")

# Check the type of my_bool
if isinstance(my_bool, bool):
    print("my_bool is of type bool")
else:
    print("my_bool is NOT of type bool")

# Check the type of my_string
if isinstance(my_string, str):
    print("my_string is of type str")
else:
    print("my_string is NOT of type str")

# Check the type of my_list
if isinstance(my_list, list):
    print("my_list is of type list")
else:
    print("my_list is NOT of type list")

# Check the type of my_dict
if isinstance(my_dict, dict):
    print("my_dict is of type dict")
else:
    print("my_dict is NOT of type dict")

print()
print("subclasses of built-in types")
print()

# Print the subclasses of my_int
print("Subclasses of my_int:")
print(type(my_int).__subclasses__())

# Print the subclasses of my_float
print("Subclasses of my_float:")
print(type(my_float).__subclasses__())

# Print the subclasses of my_bool
print("Subclasses of my_bool:")
print(type(my_bool).__subclasses__())

# Print the subclasses of my_string
print("Subclasses of my_string:")
print(type(my_string).__subclasses__())

# Print the subclasses of my_list
print("Subclasses of my_list:")
print(type(my_list).__subclasses__())

# Print the subclasses of my_dict
print("Subclasses of my_dict:")
print(type(my_dict).__subclasses__())
