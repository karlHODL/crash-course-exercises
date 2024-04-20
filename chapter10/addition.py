print("Give me two numbers, and I'll add them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    try:
        result = int(first_number) + int(second_number)
    except ValueError:
        print("Please enter numbers, not text.")
    else:
        print(f"The result is {result}.")