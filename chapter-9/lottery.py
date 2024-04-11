from random import choice

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]
selected_values = []
count = 0

class LotteryTicket:
    """A simple class representing a lottery ticket."""
    def __init__(self):
        self.selected_values = selected_values

    def select_values(self):
        """Select 4 values from the list of possible values."""
        for _ in range(4):
            value = choice(values)
            self.selected_values.append(value)
        return self.selected_values

winning_ticket = LotteryTicket()
winning_numbers = winning_ticket.select_values()[:]
print(winning_numbers)

while True:
    count += 1
    selected_values = []
    ticket = LotteryTicket()
    ticket_numbers = ticket.select_values()
    if ticket_numbers == winning_numbers:
        print(f"\nCongratulations! You won the lottery after {count} tickets!")
        break
    elif count % 100000 == 0:
        print(f"\nYou have bought {count} tickets so far. Keep going!")
        print(ticket_numbers)