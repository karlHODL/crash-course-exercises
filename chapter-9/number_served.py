class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, increment):
        """Increment the number of customers served."""
        if increment >= 0:
            self.number_served += increment
        else:
            print("You can't roll back the number served!")

restaurant = Restaurant('The Sunken Well', 'American')

print(f"Welcome to {restaurant.restaurant_name}!")
print(f"We serve {restaurant.cuisine_type} food.")

print(f"Number served: {restaurant.number_served}")
restaurant.number_served = 10
print(f"Number served: {restaurant.number_served}")

restaurant.set_number_served(20)
print(f"Number served: {restaurant.number_served}")

restaurant.increment_number_served(5)
print(f"Number served: {restaurant.number_served}")

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant2 = Restaurant('The Blue Moose', 'Italian')
# restaurant3 = Restaurant('The Red Pepper', 'Mexican')

# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()