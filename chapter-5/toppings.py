topping = 'banana peppers'
if topping != 'anchovies':
    print("Hold the anchovies!")

requested_toppings = ['mushrooms', 'onions', 'pineapple']
# requested_toppings = []
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)

if 'mushrooms' in requested_toppings:
    print('Adding mushrooms.')
if 'pepperoni' in requested_toppings:
    print('Adding pepperoni.')
if 'pineapple' in requested_toppings:
    print('Adding pineapple.')
print("\nFinished making your pizza!")

if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping == 'green peppers':
            print("Sorry, we're out of green peppers right now.")
        else:
            print(f"Adding {requested_topping}.")
else:
    print("Are you sure you want a plain pizza?")

available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")