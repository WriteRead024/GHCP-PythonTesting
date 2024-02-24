
### GHCP-PythonTesting

This project subfolder contains coding work intended to develop understanding of unit testing in the Python programming language.&nbsp;
The unit test files in this PythonUnitTesting directory are in the 'unittest' module style 
and can be run using the 'run-python-unittest.sh' script.

# Unit Test Framework Comparison

The three unit test frameworks recommended by GitHub Copilot on Feb. 21, 2024 were:

1) unittest

2) pytest

3) nose

Here is information about each of them.&nbsp;
There is also info about the **'doctest'** module at the end of this 'md' file.


## unittest

Referencing the documentation for ['unittest' on the docs.python.org websites](https://docs.python.org/3/library/unittest.html)
it seems that the built-in (a fresh "pip list | grep test" returned no matches but an interactive "import unittest" worked fine) 
unittest functionality is built around the object-oriented concepts of test fixture, test case, test suite, and test runner.

It looks like test cases are denoted by a 'test_' prefix on a function 'def' definition.

It looks like test class is denoted by a '(unittest.TestCase)' class definition parameter.

It looks like test files are by convention denoted with a 'test_' filename prefix or '_test' filename suffix.&nbsp; 
The unittest [test discovery](https://docs.python.org/3/library/unittest.html#unittest-test-discovery) 
feature uses 'test*.py' as the default pattern matcher.

The Python rules for identifier validity (at [lexical analysis identifiers](https://docs.python.org/3/reference/lexical_analysis.html#identifiers)) 
define what a valid filename is&nbsp;  Valid filenames are required for detection by the TestLoader, new to Python 3.2.&nbsp; 

"Caution, test discovery loads tests by importing them."&nbsp; 
The implementation for test discovery has been revised at least twice since Python 3.3.&nbsp; 
([unittest doc](https://docs.python.org/3/library/unittest.html))&nbsp; 

The finest useful granularity of Python 'unittest' units is probably the "assert methods".&nbsp;
A reference list for the assert methods is at 
[Python unittest assert methods list](https://docs.python.org/3/library/unittest.html#assert-methods).


## pytest

At first glance, 'pytest' appears to be in [version 8.0, from the website URI](https://docs.pytest.org/en/8.0.x/contents.html).&nbsp; 
[pytest requires Python 3.8+ or PyPy3.](https://docs.pytest.org/en/8.0.x/).&nbsp; 
pytest requires a separate 'pip install -U pytest' (the "-U" upgrades all packages to their latest version).

It looks like pytest expects files with tests to be prefixed 'test_'.

I did not explore 'pytest' further at all.


## nose

GitHub Copilot disclaimed its recommendation of the nose framework as not actively maintained.&nbsp; 

It turned out that there is a newer version, "nose2" that has GitHub commits as recently as three weeks before Feb. 2024.&nbsp; 
The GitHub project was at: [nose-devs/nose2](https://github.com/nose-devs/nose2).

The [GitHub C.I. for nose2](https://github.com/nose-devs/nose2/actions?query=workflow%3Abuild) 
badge link showed it was passing ~252 of its 259 build workflow tasks, the other five badges seemed to indicate 
up-to-date maintenance.&nbsp; The original "nose" project on GitHub had no readme badge links.&nbsp; 

From what I initially gathered from the nose2 readme, nose2 is like an extension to the built-in unittest features.


## doctest

A Python library module '[doctest.py](https://docs.python.org/3/library/doctest.html#module-doctest)'
was mentioned in the Python unittest documentation ([unittest](https://docs.python.org/3/library/unittest.html)).

According to that documentation for the module, the purpose of the doctest module is to verify that an 
interactive [REPL type] Python session works the same as recorded in a "docstrings" example.&nbsp; 
More info about Python Docstrings at the Python Enhancement Proposal for the Docstrings convention at 
[PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/).

It is probably inconvenient to include all of the unit tests for Python code in Docstring comments, 
but the idea that tests could be included in them is good.