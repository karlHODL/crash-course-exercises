class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

restaurant = Restaurant('The Sunken Well', 'American')

print(f"Welcome to {restaurant.restaurant_name}!")
print(f"We serve {restaurant.cuisine_type} food.")

restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant2 = Restaurant('The Blue Moose', 'Italian')
restaurant3 = Restaurant('The Red Pepper', 'Mexican')

restaurant2.describe_restaurant()
restaurant3.describe_restaurant()