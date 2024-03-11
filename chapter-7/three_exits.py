# topping = ''
# while topping != 'quit':
#     topping = input("\nEnter a pizza topping:\n"
#                     "Enter 'quit' to end the program. ")
#     if topping != 'quit':
#         print(f"\nAdding {topping} to your pizza.")

active = True

while active:
    age = int(input("\nEnter your age: "))
    if age == 0:
        active = False
    elif age < 3:
        print("\nYour ticket is free.")
    elif age < 13:
        print("\nYour ticket is $10.")
    else:
        print("\nYour ticket is $15.")