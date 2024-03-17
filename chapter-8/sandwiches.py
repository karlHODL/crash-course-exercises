def make_sandwich(*ingredients):
    """Print the list of ingredients that have been requested."""
    print("\nMaking a sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"\t- {ingredient}")

make_sandwich('ham')
make_sandwich('turkey', 'lettuce', 'tomato')
make_sandwich('peanut butter', 'jelly')