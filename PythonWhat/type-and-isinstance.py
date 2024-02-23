
# Feb. 23, 2024
# Rich W.
# with GitHub CoPilot
# MSL.l

print("Defining the Fruit class and Citrus subclass of the Fruit class.")
class Fruit:
    pass

class Citrus(Fruit):
    pass

print("Instantiating a fresh_fruit object as a Citrus.")
fresh_fruit = Citrus()

# Using type()
print("type(fresh_fruit) == Citrus")
print(type(fresh_fruit) == Citrus)  # True
print("type(fresh_fruit) == Fruit")
print(type(fresh_fruit) == Fruit)   # False

# Using isinstance()
print("isinstance(fresh_fruit, Citrus)")
print(isinstance(fresh_fruit, Citrus))  # True
print("isinstance(fresh_fruit, Fruit)")
print(isinstance(fresh_fruit, Fruit))   # True

