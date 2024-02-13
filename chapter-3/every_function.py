mountains = ['Mount Everest', 'K2', 'Kangchenjunga', 'Lhotse', 'Makalu']
print(mountains)

print(sorted(mountains))
print(mountains)

print(len(mountains))
print()
mountains.reverse()
print(mountains)
print(mountains.sort())

mountains.pop()
print(mountains)

mountains.remove('Kangchenjunga')
print(mountains)

mountains.insert(2, 'Kangchenjunga')
mountains.append('Rainier')
print(mountains)

del mountains[0]
print(mountains)