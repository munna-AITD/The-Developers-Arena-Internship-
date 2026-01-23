#Indentation in Python 
"""Python Indentation refers to the use of whitespace (spaces or tabs) at
the beginning of code line. It is used to define the code blocks.
Indentation is crucial in Python because, unlike many other programming
languages that use braces "{}" to define blocks, Python uses indentation.
It improves the readability of Python code, but on other hand it became
difficult to rectify indentation errors."""
###Python Variables####
"Variables in Python are essentially named references pointing to objects in memory."
"Variable can be start with alphabetical letter not start with a number"
a = 10
print(type(a))
b = "Python String"
print(type(b))
            ##Python Identifiers##
"""In Python, identifiers are unique names that are assigned to variables, 
functions, classes, and other entities. They are used to uniquely identify 
the entity within the program. They should start with a letter (a-z, A-Z) 
or an underscore "_" and can be followed by letters, numbers, or underscores.
In the below example "first_name" is an identifier that store string value."""
first_name = "Ram"
###########Python keywords####
"""Keywords in Python are reserved words that have special meanings and 
serve specific purposes in the language syntax. They cannot be used as 
identifiers (names for variables, functions, classes, etc.). For instance,
 "for", "while", "if", and "else" are keywords and cannot be used as 
 identifiers."""
#####Comments in Python###
"""Comments in Python are statements written within the code. They are 
meant to explain, clarify, or give context about specific parts of the code."""
# Single line comments
'Single line comments are preceded by the "#" symbol. Everything after'
'this symbol on the same line is considered a comment.'
first_name = "Munna"
last_name = "Kumar"  # assign last name

# print full name
print(first_name, last_name)
##Python Multi-line Comment##
'''
Multi Line comment.
Code will print name.
'''
f_name = "Alen"
print(f_name)
#Multiple Line Statements
sentence = "This is a very long sentence that we want to " \
           "split over multiple lines for better readability."

print(sentence)
# For mathematical operations
total = 1 + 2 + 3 + \
        4 + 5 + 6 + \
        7 + 8 + 9
print(total)
#Continuation of Statements in Python
'''Python implicitly supports line continuation within parentheses (), 
square brackets [], and curly braces {}. This is often used in defining 
multi-line lists, tuples, dictionaries, or function arguments.'''
#Implicit Continuation
# Line continuation within square brackets '[]'
numbers = [
    1, 2, 3,
    4, 5, 6,
    7, 8, 9
]
print(numbers)

# Explicit continuation
s = "GFG is computer science portal " \
    "by Geeks, used by Geeks."
print(s)
#Taking Input from User in Python
# Taking input from the user
name = input("Please enter your name: ")
# Print the input
print(f"Hello," + name)
