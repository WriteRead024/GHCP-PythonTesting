# Feb. 23, 2024
# GitHub CoPilot
# with Rich W.
# MSL.l


# Define a metaclass
class NewMetaclass(type):
    def __new__(cls, name, bases, attrs):
        # Modify the attributes of the class
        attrs["custom_attr"] = "This is a custom attribute of the MyMeta class."

        def describe_what_is_happening(self):
            print(
                "NewMetaclass is a metaclass because it is an extension of the 'type' metaclass."
            )

        attrs["describe_what_is_happening"] = describe_what_is_happening
        return super().__new__(cls, name, bases, attrs)


# Create a class using the metaclass
class MyClass(metaclass=NewMetaclass):
    pass


# Create an instance of the class
my_obj = MyClass()

# describe what is happening
my_obj.describe_what_is_happening()
# Output: NewMetaclass is a metaclass because it is an extension of the 'type' metaclass.

# Access the custom attribute added by the metaclass
print(my_obj.custom_attr)  # Output: This is a custom attribute of the MyMeta class.


# Define a regular class
class MyRegularClass:
    def __init__(self):
        self.custom_attr = (
            "This is a reassigned custom attribute value of the MyRegularClass class."
        )


# Create an instance of the regular class
my_regular_obj = MyRegularClass()

# Access the custom attribute of the regular class
print(
    my_regular_obj.custom_attr
)  # Output: This is a reassigned custom attribute value of the MyRegularClass class.
