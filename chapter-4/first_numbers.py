for value in range(1, 6):
    print(value)

numbers = list(range(1,6))
print(numbers)

even_numbers = list(range(2, 21, 2))
print(even_numbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)
print()

squares = [value ** 2 for value in range(1, 11)]
print(squares)

digits = list(range(11))
print(min(digits))
print(max(digits))
print(sum(digits))