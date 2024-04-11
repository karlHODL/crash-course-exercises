"""A set of classes representing restaurant types."""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} food.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

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