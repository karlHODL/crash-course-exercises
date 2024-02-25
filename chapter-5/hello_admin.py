current_users = ['bear', 'bama', 'Brian', 'Billy', 'roger']
new_users = ['billy', 'Bobby', 'Roger', 'tom', 'jerry']
users = ['admin', 'bear', 'bama', 'brian', 'billy']
# users = []

if users:
    for user in users:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, welcome back!")
else:
    print("We need to find some users!")

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"Sorry {new_user.title()}, that username is already taken.")
    else:
        print(f"Great, {new_user.title()} is available!")