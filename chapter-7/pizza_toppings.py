while True:
    topping = input("\nEnter a pizza topping:\n"
                    "Enter 'quit' to end the program. ")
    if topping == 'quit':
        break
    else:
        print(f"\nAdding {topping} to your pizza.")