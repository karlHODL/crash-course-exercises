from random import randint

class Die:
    """A simple class representing a die of n sides."""
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Roll the die and print the result."""
        print(randint(1, self.sides))

six_sided_die = Die()
for _ in range(10):
    six_sided_die.roll_die()
print("\n")

ten_sided_die = Die(10)
for _ in range(10):
    ten_sided_die.roll_die()
print("\n")

twenty_sided_die = Die(20)
for _ in range(10):
    twenty_sided_die.roll_die()