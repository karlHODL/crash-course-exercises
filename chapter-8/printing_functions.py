def print_models(to_print, printed):
    while to_print:
        new_print = to_print.pop()
        printed.append(new_print)
        print(f"\nPrinting {new_print}.")

def print_summary(complete_models):
    print("\nThe following models have been printed:")
    for model in complete_models:
        print(f"\t- {model}")