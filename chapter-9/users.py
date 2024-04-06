class Users:
    def __init__(self, first_anme, last_name, age, location):
        self.first_name = first_anme
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name} is {self.age} years old and " 
               f"lives in {self.location}.")
        
    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0

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


user1 = Users('John', 'Doe', 25, 'New York')

admin = Admin('Jane', 'Smith', 30, 'Los Angeles')
admin.privileges.show_privaleges()

# user1.describe_user()
# user1.greet_user()

# user1.increment_login_attempts()
# user1.increment_login_attempts()
# user1.increment_login_attempts()

# print(f"Login attempts: {user1.login_attempts}")

# user1.reset_login_attempts()
# print(f"Login attempts: {user1.login_attempts}")
