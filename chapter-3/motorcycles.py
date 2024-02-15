def print_motorcycles():
    for motorcycle in motorcycles:
        print(motorcycle)

motorcycles = ['honda', 'yamaha', 'suzuki']

# Add an element to the list using the append() method
motorcycles.append('ducati')
print_motorcycles()
print()

# Add an element to the list using the insert() method
motorcycles.insert(1, 'harley-davidson')
print_motorcycles()
print()

# Remove an item from the list using the del statement
del motorcycles[0]
print_motorcycles()
print()

# Remove an item from the list using the pop() method
popped_cycle = motorcycles.pop()
print_motorcycles()
print()
print(popped_cycle)

second_motorcycle = motorcycles.pop(1)
message = f"\nThe second motorcycle I owned was a {second_motorcycle.title()}."
print(message)

# Remove an item from the list using the remove() method
sold_motorcycle = 'suzuki'
motorcycles.remove(sold_motorcycle)
print_motorcycles()
message = f"\nI used to own a {sold_motorcycle.title()} motorcycle, but I sold it."
print(message)

