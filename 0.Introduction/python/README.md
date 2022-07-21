# Python

[Python](https://www.python.org/) is a very powerful and widely-used language that will allow us to quickly build fairly complicated web applications. If Python is not installed, please install it [here](https://www.python.org/downloads/). Another tool that comes with Python is pip, download it [here](https://pip.pypa.io/en/stable/installation/) as it will be needed later in the course

## Hello, World!

Any programming language starts with printing "Hello, World". In Python, it is very simple, the build-in function print() can output the argument to the terminal

`print("Hello, World!")`

Different from C++/C or Java, Python uses an interpreter instead of a compiler. Interpreter comes with the Python installation, when one uses the command `python somefile.py`, the interpreter takes the _somefile.py_ file and interpret line by line what each line should be doing and convert it to machine code

## Variables

A key part of any programming language is the ability to create and manipulate variables. In order to assign a value to a variable in Python, the syntax looks like this:

```Python
a = 28
b = 1.5
c = "Hello!"
d = True
e = None
```

Each of these lines is taking the value to the right of the =, and storing it in the variable name to the left

Unlike in some other programming languages, Python variable types are inferred, meaning that while each variable does have a type, we do not have to explicitly state which type it is when we create the variable. Some of the most common variable types are:

- **int**: An integer
- **float**: A decimal number
- **chr**: A single character
- **str**: A string, or sequence of characters
- **bool**: A value that is either True or False
- **NoneType**: A special value (None) indicating the absence of a value.

## User Input

An interesting program always involves interaction with the user. In Python, user input can be taken by using the build-in input() function where the argument is what is presented in the terminal. The user will input a string, for example

```Python
name = input("Name: ")
print("Hello, " + name)
```

The input is stored in the string variable called "name" and then being printed with "Hello" concatenate to it, so the output of the program will be "Hello, {name}" where the name is entered by the user

#### Formatting String

Formatting string or fstring is introduced to simplify the syntax of Python. For instance, the above program can be rewritten as

```Python
name = input("Name: ")
print(f"Hello, {name}")
```

## Conditions

Just like in other programming languages, Python gives us the ability to run different segments of code based on different conditions. For example, in the program below, we’ll change our output depending on the number a user types in:

````Python
num = int(input("Number: "))
if num > 0:
print("Number is positive")
elif num < 0:
print("Number is negative")
else:
print("N```Pythonumber is 0")

````

The int() outside of input() is to convert input string to an integer since the conditions are comparing the input to integers and string cannot compare with integers. The above program will print different sentences based on the number user input

## Sequences

One of the most powerful parts of the Python language is its ability to work with sequences of data in addition to individual variables

There are several types of sequences that are similar in some ways, but different in others. When explaining those differences, we’ll use the terms mutable/immutable and ordered/unordered. Mutable means that once a sequence has been defined, we can change individual elements of that sequence, and ordered means that the order of the objects matters

### Strings

**Ordered**: Yes **Mutable**: No

We’ve already looked at strings a little bit, but instead of just variables, we can think of a string as a sequence of characters. This means we can access individual elements within the string! For example:

```Python
name = "Harry"
print(name[0]) # "H"
print(name[1]) # "a"
```

### Lists

**Ordered**: Yes **Mutable**: Yes

A [Python list](https://www.w3schools.com/python/python_lists.asp) allows you to store any variable types. We create a list using square brackets and commas, as shown below. Similarly to strings, we can print an entire list, or some individual elements. We can also add elements to a list using `append`, and sort a list using `sort`

```Python
# This is a Python comment
names = ["Harry", "Ron", "Hermione"]
# Print the entire list:
print(names) # ["Harry", "Ron", "Hermione"]
# Print the second element of the list:
print(names[1]) # "Ron"
# Add a new name to the list:
names.append("Draco")
# Sort the list according alphabetical order:
names.sort()
# Print the new list:
print(names) # ["Draco", "Harry", "Hermione", "Ron"]
```

### Tuples

**Ordered**: Yes **Mutable**: No

[Tuples](https://www.w3schools.com/python/python_tuples.asp) are generally used when you need to store just two or three values together, such as the x and y values for a point. In Python code, we use parentheses:

```Python
point = (12.5, 10.6)
```

### Sets

**Ordered**: No **Mutable**: N/A

[Sets](https://www.w3schools.com/python/python_sets.asp) are different from lists and tuples in that they are unordered. They are also different because while you can have two or more of the same elements within a list/tuple, a set will only store each value once. We can define an empty set using the `set()` function. We can then use `add` and `remove` to add and remove elements from that set, and the `len` function to find the set’s size. Note that the len function works on all sequences in python. Also note that despite adding 4 and 3 to the set twice, each item can only appear once in a set

```Python
# Create an empty set:
s = set()

# Add some elements:
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.add(1)

# Remove 2 from the set
s.remove(2)

# Print the set:
print(s)

# Find the size of the set:
print(f"The set has {len(s)} elements.")

""" This is a python multi-line comment:
Output:
{1, 3, 4}
The set has 3 elements.
"""
```

### Dictionaries

**Ordered**: No **Mutable**: Yes

[Python Dictionaries](https://www.w3schools.com/python/python_dictionaries.asp) or `dict`s, will be especially useful in this course. A dictionary is a set of key-value pairs, where each key has a corresponding value, just like in a dictionary, each word (the key) has a corresponding definition (the value). In Python, we use curly brackets to contain a dictionary, and colons to indicate keys and values. For example:

```Python
# Define a dictionary
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
# Print out Harry's house
print(houses["Harry"])
# Adding values to a dictionary:
houses["Hermione"] = "Gryffindor"
# Print out Hermione's House:
print(houses["Hermione"])

""" Output:
Gryffindor
Gryffindor
"""
```

## Loop/Iteration

Loops are an incredibly important part of any programming language, and in Python, they come in two main forms: [for loops](https://www.w3schools.com/python/python_for_loops.asp) and [while loops](https://www.w3schools.com/python/python_while_loops.asp)

For loops are used to iterate over a sequence of elements, performing some block of code (indented below) for each element in a sequence. For example, the following code will print out the numbers from 0 to 5:

```Python
for i in [0, 1, 2, 3, 4, 5]:
    print(i)

""" Output:
0
1
2
3
4
5
"""
```

While loops are used to repeat until certain condition is met. For example

```Python
i = 0
while i < 6:
    print(i)
    i += 1

""" Output:
0
1
2
3
4
5
"""
```

## Function

We’ve already seen a few Python build-in functions such as `print` and `input`, but now we’re going to dive into writing our own functions. To get started, we’ll write a function that takes in a number and squares it:

```Python
def square(x):
    return x * x
```

Notice how we use the `def` keyword to indicate we’re defining a function, that we’re taking in a single input called `x` and that we use the `return` keyword to indicate what the function’s output should be

And then we are able to call our own function by entering the name of the function and give it an input as the function is designated:

```Python
print(square(5)) # 25
```

## Modules

As our projects get larger and larger, it will become useful to be able to write functions in one file/module and run them in another. In the case above, we could create create one file/module called `functions.py` with the code:

```Python
def square(x):
    return x * x
```

And another file/module called `square.py` with the code:

```Python
print(square(5)) # NameError: Name "square" is not defined
```

However, the terminal will give us the error message: "NameError: Name "square" is not defined". This is because Python files/modules don't know each other, we have to use `import file_name` to make use of functions written in other files/modules

Now, `square.py` looks like this:

```Python
from functions import square
print(square(5)) # 25
```

Or alternatively, we can import the entire module, then use dot to specify the function

```Python
import functions
print(functions.square(5)) # 25
```

There are many built-in Python modules we can import such as `math` or `csv` that give us access to even more functions. Additionally, we can download even more Modules to access even more functionality! We’ll spend a lot of time using the `Django` Module in this course

## Object-Oriented Programming

[Object-Oriented Programming (OOP)](https://en.wikipedia.org/wiki/Object-oriented_programming) is a programming paradigm, or a way of thinking about programming, that is centered around objects that can store information and perform actions

We’ve already seen a few different types of variables in python, but what if we want to create our own type? A Python [Class](https://www.w3schools.com/python/python_classes.asp) is essentially a template for a new type of object that can store information and perform actions. An instance of a Class is called an object. Here’s a class that defines a two-dimensional point:

```Python
class Point():
    # A method defining how to create a point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
```

Note that in the above code, we use the keyword `self` to represent the object we are currently working with. `self` should be the first argument for any method within a Python class

Now, let’s see how we can actually use the class from above to create an object:

```Python
p = Point(2, 8) # Creating a new Point object with x = 2 and y = 8
print(p.x)
print(p.y)

""" Output:
2
8
"""
```

Now, let’s look at a more interesting example where instead of storing just the coordinates of a Point, we create a class that represents an airline flight:

```Python
class Flight():
    # Method to create new flight with given capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # Method to add a passenger to the flight:
    def add_passenger(self, name):
        self.passengers.append(name)
```

However, in a real world sense, this class is flawed because while we set a capacity, we could still append in the list of passengers even if the length of the list surpasses the capacity of the flight. Let’s augment it so that before adding a passenger, we check to see if there is room on the flight:

```Python
class Flight():
    # Method to create new flight with given capacity
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    # Method to add a passenger to the flight:
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    # Method to return number of open seats
    def open_seats(self):
        return self.capacity - len(self.passengers)
```

Note that above, we use the line `if not self.open_seats()` to determine whether or not there are open seats. This works because in Python, the number 0 can be interpretted as meaning `False`, and we can also use the keyword not to signify the opposite of the following statement so `not True` is `False` and `not False` is `True`. Therefore, if `open_seats` returns 0, the entire expression will evaluate to `True`

Now, let’s try out the class we’ve created by instantiating some objects:

```Python
# Create a new flight with up to 3 passengers
flight = Flight(3)

# Create a list of people
people = ["Harry", "Ron", "Hermione", "Ginny"]

# Attempt to add each person in the list to a flight
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")

""" Output:
Added Harry to flight successfully
Added Ron to flight successfully
Added Hermione to flight successfully
No available seats for Ginny
"""
```

## Functional Programming

In addition to supporting Object-Oriented Programming, Python also supports the [Functional Programming Paradigm](https://en.wikipedia.org/wiki/Functional_programming), in which functions are treated as values just like any other variable

### Decorators

One thing made possible by functional programming is the idea of a decorator, which is a higher-order function that can modify another function. For example, let’s write a decorator that announces when a function is about to begin, and when it ends. We can then apply this decorator using an @ symbol just before the function we want to decorate. For instance

```Python
def announce(f):
    def wrapper():
        print("About to run the function")
        f()
        print("Done with the function")
    return wrapper

@announce
def hello():
    print("Hello, world!")

hello()

""" Output:
About to run the function
Hello, world!
Done with the function
"""
```

### Lambda Functions

Lambda functions provide another way to create functions in python. For example, if we want to define the same square function we did earlier, we can write:

```Python
square = lambda x: x * x
print(square(5)) # 25
```

Where the input is to the left of the : and the output is on the right

This can be useful when we don’t want to write a whole separate function for a single, small use. For example, if we want to sort some objects where it’s not clear at first how to sort them. Imagine we have a list of people, but with names and houses instead of just names that we wish to sort, since the build-in `sort` function does not support sorting by a specific value, we have to indicate which variables we wish to sort in the `sort` function. For example

```Python
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

def f(person):
    return person["name"]

people.sort(key=f)

print(people)

""" Output:
[{'name': 'Cho', 'house': 'Ravenclaw'}, {'name': 'Draco', 'house': 'Slytherin'}, {'name': 'Harry', 'house': 'Gryffindor'}]
"""
```

We specifies that the sorting is based on the key where the key is the name of each person. The key here is provided using a separate function. But using a whole function just for sorting is an overkill, that's where lambda functions come in

```Python
people = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Slytherin"}
]

people.sort(key=lambda person: person["name"])

print(people)

""" Output:
[{'name': 'Cho', 'house': 'Ravenclaw'}, {'name': 'Draco', 'house': 'Slytherin'}, {'name': 'Harry', 'house': 'Gryffindor'}]
"""
```

## Exceptions

Sometimes exceptions happen, maybe users are too wild about what they are trying to do, but programmers cannot limit what the users can do, the only thing programmers can do it to consider that exception and handle it gracefully. In the following chunk of code, we’ll take two integers from the user, and attempt to divide them:

```Python
x = int(input("x: "))
y = int(input("y: "))

result = x / y

print(f"{x} / {y} = {result}")
```

In many cases, the program works just fine; however, we’ll run into problems when we attempt to divide by 0. Instead of showing the users some messy command line error, We can deal with this messy error using [Exception Handling](https://www.w3schools.com/python/python_try_except.asp). In the following block of code, we will `try` to divide the two numbers, `except` when we get a `ZeroDivisionError`:

```Python
import sys

x = int(input("x: "))
y = int(input("y: "))

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # Exit the program
    sys.exit(1)

print(f"{x} / {y} = {result}")
```

There are other errors such as a `ValueError`, the users are supposed to enter a integer for division, but wildly enough, they entered a string like "hello, world", the program should not pop up a command line error, instead, it should gently remind the user:

```Python
import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by 0.")
    # Exit the program
    sys.exit(1)

print(f"{x} / {y} = {result}")
```

## Examples

Check out some [examples](examples/)
