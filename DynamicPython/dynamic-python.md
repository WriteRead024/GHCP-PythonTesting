
### GHCP-PythonTesting

# Dynamic Python

The "Dynamic Python" explored in this folder is not really the problem deconstruction technique
kind of dynamic programming made famous in the 1950s ([Wikipedia](https://en.wikipedia.org/wiki/Dynamic_programming)).&nbsp; 
Nor is it concerned with the dynamic program object typing paradigm that contrasts Python with the 
statically typed "C" family of programming languages (as well as others).&nbsp; 
This exploration is concerned with programmatic changes to features of the Python language
itself.&nbsp; 
The potential for confusion is perhaps amplified by the main first exploration being concerned with 
adding static-typing style language using the '[mypy](https://github.com/python/mypy)' module.&nbsp; 
Mypy is not exactly dynamic programming in the sense intended by this exploration, 
but it is an example of how Python as a programming language is being extended and improved
while maintaining some amount of backward compatibility with the flexibility of the original.

Note that static typing for Python is not necessarily a useful idea.&nbsp; 
Developer tools such as [Pyright](https://github.com/microsoft/pyright) 
can provide typechecking in the editor before precompilation/runtime, 
and Python itself has several typechecking features built-in as part of new 
versions of the language (such as Type Hints for method arguments and returns types).&nbsp; 

The point here is that programmatic dynamicity is one of the main advantages gained 
from the flexibility that Python offers.&nbsp; 
To put it in another and terrible backwards analogy way, 
if your program code has no feet, then it can't shoot them.&nbsp; 
<!-- (Though the problem of Python accidentally 
eating stray bullet lead from the ground without
knowing better seems to remain). -->