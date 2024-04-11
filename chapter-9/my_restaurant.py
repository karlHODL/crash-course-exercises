from restaurant import Restaurant

class IceCreamStand(Restaurant):
    """Represents aspects of a restaurant, specific to ice cream stands."""
    def __init__(self, restaurant_name, cuisine_type='Ice Cream'):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def list_flavors(self):
        """Print a list of ice cream flavors."""
        print("We have the following flavors available:")
        for flavor in self.flavors:
            print(f"\t{flavor}")

my_restaurant = Restaurant('The Sunken Well', 'American')
my_restaurant.describe_restaurant()

# print(f"Welcome to {restaurant.restaurant_name}!")
# print(f"We serve {restaurant.cuisine_type} food.")

# restaurant.describe_restaurant()
# restaurant.open_restaurant()

# restaurant2 = Restaurant('The Blue Moose', 'Italian')
# restaurant3 = Restaurant('The Red Pepper', 'Mexican')

# restaurant2.describe_restaurant()
# restaurant3.describe_restaurant()

# ice_cream_stand = IceCreamStand('Scoops')
# ice_cream_stand.list_flavors()