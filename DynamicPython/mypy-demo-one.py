# Feb. 2024
# Rich W.


# The type hints here are detected by mypy
# and mypy will report an error when it scans this file.
def simple_concat(a: str, b: int) -> str:
    return a + b


# this series of statements will only
# cause one mypy error on the last line
name: str = "example name"
age: int = 42
name_and_age_one = simple_concat(name, age)
name_and_age_two = name + age
