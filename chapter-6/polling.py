favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

take_poll = ['jen', 'phil', 'stewart', 'marshall', 'randy']

for name in take_poll:
    if name in favorite_languages.keys():
        print(f"Thank you for taking the poll, {name.title()}!")
    else:
        print(f"Please take the poll, {name.title()}!")