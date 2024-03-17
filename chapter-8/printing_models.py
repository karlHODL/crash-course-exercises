unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
printed_models = []

def print_models(to_print, printed):
    while to_print:
        new_print = to_print.pop()
        printed_models.append(new_print)
        print(f"\nPrinting {new_print}.")

def print_summary(complete_models):
    print("\nThe following models have been printed:")
    for model in complete_models:
        print(f"\t- {model}")


copy_designs = unprinted_designs[:]
print_models(copy_designs, printed_models)
print_summary(printed_models)
print(unprinted_designs) 

# print_models(unprinted_designs, printed_models)
# print_summary(printed_models)