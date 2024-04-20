from pathlib import Path
import json

def get_stored_user(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user = json.loads(contents)
        return user
    else:
        return None
    
def get_new_user(path):
    """Prompt the user for a username and store it."""
    username = input("What is your name? ")
    zipcode = input("What is your zipcode? ")
    age = input("What is your age? ")
    user = {'username': username, 'zipcode': zipcode, 'age': age}
    contents = json.dumps(user)
    path.write_text(contents)
    return user

def greet_user():
    """Greet the user by name."""
    path = Path('user.json')
    user = get_stored_user(path)
    if user:
        # print portions the dictionary
        check = input(f"Is {user['username']} your name? (yes/no) ")
        if check == 'yes':
            print(f"Welcome back, {user['username']} ({user['age']}) from {user['zipcode']}!")
        else:
            user = get_new_user(path)
            print(f"We'll remember you when you come back, {user['username']}!")
    else:
        user = get_new_user(path)
        print(f"We'll remember you when you come back, {user['username']}!")

greet_user()