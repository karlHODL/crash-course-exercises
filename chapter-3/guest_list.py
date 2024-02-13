def print_guest_list():
    total_guests = len(guests)
    print(f"We have {total_guests} guests coming to dinner.\n")
    for guest in guests:
        greeting = f"Hello, {guest.title()}! You are invited to a dinner party.\n"
        print(greeting)

def print_notifications():
    for i in range(len(guests)):
        if len(guests) < 3:
            break
        uninvited = guests.pop()
        notification = f"Hello, {uninvited}! Unfortunately, there's no longer room at the dinner party. I hope you can attend another time.\n"
        print(notification)

guests = ['Ricky Gervais', 'Tim Ferriss', 'Elon Musk', 'Balaji Srinivasan', 'Amjad Masad']
print_guest_list()

# New invitations after removal
removed_guest = guests.pop(2)
print(f"{removed_guest} can't make it to the dinner party.\n")

print_guest_list()

# New inviations after finding a larger table
print("We found a larger table!\n")

guests.insert(0, 'Mike Solana')
guests.insert(2, 'Joe Rogan')
guests.append('Naval Ravikant')

print_guest_list()

# New invitatioins and notifications after finding smaller table
print("We can only invite two guests to dinner.\n")

# Print the notifications of those that were uninvited
print_notifications()

# Print the final guest invitations
print_guest_list()

# Remove the remaining guests
del guests[1]
del guests[0]

# Print the empty list
print(guests)

