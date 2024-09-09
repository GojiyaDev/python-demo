#function as "first class citizens"
#you can assign the function to variable
"""def square(x):

    return x * x #Assigning a function to a variable


f = square
print(f(5))  # Output: 25Passing a function as an argument


def apply_function(func, value):
    return func(value)
result = apply_function(square, 4)
print(result)  # Output: 16"""

#other example
"""def double(x):

    return x * 2
def triple(x):
    return x * 3
def apply_operation(func, number):
    return func(number)
print(apply_operation(double, 5))  # Output: 10
print(apply_operation(triple, 5))  # Output: 15
"""

#lambda Function
#lambda function to add two number

"""add = lambda a, b: a + b
print(add(3, 5))  # Output: 8Using a lambda function with map
numbers = [1, 2, 3, 4]
squared = map(lambda x: x * x, numbers)
print(list(squared))  # Output: [1, 4, 9, 16]
"""

#list comprehension
# Example: Creating a list of squares of even numbers from 0 to 9
#without list comprehension
"""squares = []
for i in range(10):
    if i % 2 == 0:
        squares.append(i ** 2)
print(squares)"""

#with list comprehension
# The same functionality using list comprehension
"""
squares = [i ** 2 for i in range(10) if i % 2 == 0]
print(squares)
"""

#Map and Filter
# Using map to square each number in a list
"""
numbers = [1, 2, 3, 4, 5]
squared = map(lambda x: x * x, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]Using filter to get only even numbers from a list

even_numbers = filter(lambda x: x % 2 == 0, numbers)
print(list(even_numbers))  # Output: [2, 4]

"""
