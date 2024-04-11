"""A module that contains the class for admins and their roles."""
from user import Users

class Privaleges:
    """A simple attempt to model a user's privileges."""
    def __init__(self):
        self.privaleges = ['can add post', 'can delete post', 'can ban user']

    def show_privaleges(self):
        """Print a list of privileges the user has."""
        print("The user has the following privileges:")
        for privalege in self.privaleges:
            print(f"\t- {privalege}")

class Admin(Users):
    """Represents aspects of a user, specific to admin."""
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privaleges()