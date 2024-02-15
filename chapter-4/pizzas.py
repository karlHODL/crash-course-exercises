pizzas = ['pepperoni', 'veggie', 'brooklyn style']
for pizza in pizzas:
    print(f"I like {pizza} pizza.")

print("I really love pizza!")

friends_pizzas = pizzas[:]

pizzas.append('jpc')
friends_pizzas.append('hawaiian')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)