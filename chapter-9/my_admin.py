from roles import Users, Privaleges, Admin

# user1 = Users('John', 'Doe', 25, 'New York')

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
