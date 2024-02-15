my_foods = ['pizza', 'hamburger', 'tuna', 'tacos', 'sushi']
friends_foods = my_foods[:] # if you don't use the slice operator, you'll just be copying the reference to the list

my_foods.append('carrot cake')
friends_foods.append('salad')

print(my_foods)
print(friends_foods)

print("The first three items in my list are:")
for food in my_foods[:3]:
    print(food)

print("\nThree items from the middle of my list are:")
for food in my_foods[1:4]:
    print(food)

print("\nThe last three items in my list are:")
for food in my_foods[-3:]:
    print(food)
