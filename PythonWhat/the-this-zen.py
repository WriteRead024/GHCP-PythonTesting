
# Feb. 21, 2024
# Rich W.
# with GitHub CoPilot
# MSL.l
#
# adaptations from
# https://stackoverflow.com/questions/1218933/can-i-redirect-the-stdout-into-some-sort-of-string-buffer


import sys
from io import StringIO

verbose_output = True

# the "Zen of Python" expected string
expected_string = """
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""
# trimmed of leading and trailing whitespace
expected_string = expected_string.strip()


# redirect stdout to a string buffer
old_stdout = sys.stdout
sys.stdout = mystdout = StringIO()

import this

# get the string from the buffer 
# and strip leading and trailing whitespace
result_string = mystdout.getvalue()
result_string = result_string.strip()

# restore stdout
sys.stdout = old_stdout


if expected_string != result_string:
    print("Strings do not match")
    if verbose_output:
        print("expected_string: ", expected_string)
        print("result_string: ", result_string)
    print("    expected_string length: ", len(expected_string))
    print("    result_string length: ", len(result_string))
else:
    print("Expected and 'import this' result strings match.")

