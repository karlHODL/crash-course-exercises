import printing_functions as pf

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
printed_models = []


copy_designs = unprinted_designs[:]
pf.print_models(copy_designs, printed_models)
pf.print_summary(printed_models)
print(unprinted_designs) 

# print_models(unprinted_designs, printed_models)
# print_summary(printed_models)