glossary = {
    'list': 'A collection of items in a particular order.',
    'tuple': 'An immutable list.',
    'dictionary': 'A collection of key-value pairs.',
    'string': 'A series of characters.',
    'comment': 'A note in a program that the Python interpreter ignores.',
    'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'loop': 'Work through a collection of items, one at a time.',
    'conditional test': 'A comparison between two values.',
    'boolean expression': 'An expression that evaluates to True or False.',
}

# print(f"List:\n\t{glossary['list']}")
# print(f"\nTuple:\n\t{glossary['tuple']}")
# print(f"\nDictionary:\n\t{glossary['dictionary']}")
# print(f"\nString:\n\t{glossary['string']}")
# print(f"\nComment:\n\t{glossary['comment']}")

# clean up the output using a for loop
for term, definition in glossary.items():
    print(f"\n{term.title()}\n\t{definition}")