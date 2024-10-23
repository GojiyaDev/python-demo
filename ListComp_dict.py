#A Creating A list of Square
squares = [x**2 for x in range(10)]
print(squares)

#B filter even number
evens = [x for x in range(20) if x % 2 == 0]
print(evens)

#C applying function to list Element
fruits = ['apple', 'banana', 'cherry']
fruit_lengths = [len(fruit) for fruit in fruits]
print(fruit_lengths)

#D Nested List Comprehension 
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)
