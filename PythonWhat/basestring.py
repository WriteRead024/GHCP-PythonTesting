# Feb. 23, 2024
# Rich W.
# with GitHub CoPilot
# MSL.l

import sys

# Print Python version
print()
print("current Python version:", sys.version)

# Check if basestring is defined
print()
print("checking if basestring is defined in the current environment globals()")
if "basestring" in globals():
    print("basestring is defined, ")
    print("which is expected in Python 2.x")
else:
    print("basestring is not defined.")
    print("(expected in Python 3.x)")

print()
print("The purpose of the basestring class was ")
print("to allow a single test to check for both str and unicode.")
print()
