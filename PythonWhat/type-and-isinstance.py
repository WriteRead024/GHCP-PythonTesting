
# Feb. 23, 2024
# Rich W.
# with GitHub CoPilot
# MSL.l

print("Defining the Fruit class and Citrus subclass of the Fruit class.")
class Fruit:
    pass

class Citrus(Fruit):
    pass

print("Instantiating an orange as a Citrus object.")
orange = Citrus()

# Using type()
print("type(fresh_fruit) == Citrus")
print(type(orange) == Citrus)  # True
print("type(fresh_fruit) == Fruit")
print(type(orange) == Fruit)   # False

# Using isinstance()
print("isinstance(fresh_fruit, Citrus)")
print(isinstance(orange, Citrus))  # True
print("isinstance(fresh_fruit, Fruit)")
print(isinstance(orange, Fruit))   # True

