favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah']

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

for name in favorite_languages.keys():
    print(f"\nHi, {name.title()}!")
    if name in friends:
        print(f"{name.title()}, I see you like {favorite_languages[name].title()}.")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!\n")

# sort the keys in a dictionary
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# look at the values in a dictionary
print("\nThe following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())

print("\nThe following responses have been provided:")
for language in favorite_languages.values():
    print(language.title())