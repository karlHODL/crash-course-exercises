def make_pizza(size, *toppings):
    """Print the list of toppings that have been requested."""
    print(f"\nMaking a {size}-pizza with the following toppings:")
    for topping in toppings:
        print(f"\t- {topping}")

make_pizza('L', 'pepperoni')
make_pizza('M', 'mushrooms', 'green peppers', 'extra cheese')