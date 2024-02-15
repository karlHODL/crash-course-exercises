players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:4])
print(players[1:4])
print(players[:3])
print(players[2:])
print(players[-3:])

print("Here are the first two players on my team:")
for player in players[:2]:
    print(player.title())

scores = [17, 73, 56, 42, 99, 6, 35]
for score in sorted(scores)[-3:]:
    print(score)

top_scores = [value for value in sorted(scores)[-3:]]
print(top_scores)

print(scores)