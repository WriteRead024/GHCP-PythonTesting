
# Feb. 21, 2024
# Rich W.
# with GitHub CoPilot
# MSL.l

import sys
import unittest
import warnings

# expected version of Python
expected_version = "3.12.1"


# Get input arguments
print_all = any(arg == "--print-all" for arg in sys.argv[1:])
print_present = any(arg == "--present" for arg in sys.argv[1:])
quieter = any(arg == "--quieter" for arg in sys.argv[1:])
# print_missing = any(arg == "--missing" for arg in sys.argv[1:])
print_missing = True

if not quieter:
    print("unittest-attributes.py starting...")

# Compare the available version of Python with the expected_version variable
if not sys.version.startswith(expected_version):
    warningstring = f"Expected Python version {expected_version}, but found {sys.version}"
    warnings.warn(warningstring, UserWarning)
elif not quieter: 
    print(f"Expected Python version {expected_version} is detected.")


# expected non-underscored module attributes
expected_non_underscored_module_attributes = [
    "BaseTestSuite",
    "FunctionTestCase",
    "IsolatedAsyncioTestCase",
    "SkipTest",
    "TestCase",
    "TestLoader",
    "TestProgram",
    "TestResult",
    "TestSuite",
    "TextTestResult",
    "TextTestRunner",
    "addModuleCleanup",
    "case",
    "defaultTestLoader",
    "doModuleCleanups",
    "enterModuleContext",
    "expectedFailure",
    "findTestCases",
    "getTestCaseNames",
    "installHandler",
    "loader",
    "main",
    "makeSuite",
    "registerResult",
    "removeHandler",
    "removeResult",
    "result",
    "runner",
    "signals",
    "skip",
    "skipIf",
    "skipUnless",
    "suite",
    "util"
]

# expected underscored module attributes
expected_underscored_module_attributes = [
    "__all__",
    "__builtins__",
    "__cached__",
    "__dir__",
    "__doc__",
    "__file__",
    "__getattr__",
    "__loader__",
    "__name__",
    "__package__",
    "__path__",
    "__spec__",
    "__unittest"
]


# Get the module attributes
non_underscored_module_attributes = [attr for attr in dir(unittest) if not attr.startswith('__')]
underscored_module_attributes = [attr for attr in dir(unittest) if attr.startswith('__')]


# Compare the lists of attributes with the expected attributes
missing_non_underscored_attributes = set(expected_non_underscored_module_attributes) - set(non_underscored_module_attributes)
missing_underscored_attributes = set(expected_underscored_module_attributes) - set(underscored_module_attributes)


# Print the appropriate lists of results
if print_all or print_present:
    # Print the non-underscored module attributes
    print("Non-underscored module attributes:")
    for attribute in non_underscored_module_attributes:
        print(attribute)

    # Print the underscored module attributes
    print("Underscored module attributes:")
    for attribute in underscored_module_attributes:
        print(attribute)

if print_all or print_missing:
    # Print the missing non-underscored attributes
    print("Missing non-underscored attributes:")
    if (any(missing_non_underscored_attributes)):
        for attribute in missing_non_underscored_attributes:
            print(attribute)
    else:
        print("None")

    # Print the missing underscored attributes
    print("Missing underscored attributes:")
    if (any(missing_underscored_attributes)):
        for attribute in missing_underscored_attributes:
            print(attribute)
    else:
        print("None")

if not quieter:
    print("unittest-attributes.py done.")