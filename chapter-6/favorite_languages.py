favorite_languages = {
    'jen': ['python','rust'],
    'sarah': ['c'],
    'edward': ['ruby','go'],
    'phil': ['python','haskell'],
}

friends = ['phil', 'sarah']


for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
    else:
        print(f"\n{name.title()}'s favorite language is:")
    for language in languages:
        print(f"\t{language.title()}")

# for name in favorite_languages.keys():
#     print(f"\nHi, {name.title()}!")
#     if name in friends:
#         print(f"{name.title()}, I see you like {favorite_languages[name].title()}.")

# if 'erin' not in favorite_languages.keys():
#     print("Erin, please take our poll!\n")

# # sort the keys in a dictionary
# for name in sorted(favorite_languages.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# # look at the values in a dictionary
# print("\nThe following languages have been mentioned:")
# for language in set(favorite_languages.values()):
#     print(language.title())

# print("\nThe following responses have been provided:")
# for language in favorite_languages.values():
#     print(language.title())