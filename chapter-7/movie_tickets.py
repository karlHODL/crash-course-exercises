while True:
    age = int(input("\nEnter your age:"
                    "Enter '0' to end the program. "))
    if age == 0:
        break
    elif age < 3:
        print("\nYour ticket is free.")
    elif age < 13:
        print("\nYour ticket is $10.")
    else:
        print("\nYour ticket is $15.")