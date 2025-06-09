players = ['charles','martina','michael','florence','eli']
tplayers = ("charles","martina","michael","florence","eli")
lstplayers = tplayers.split(",")
print(f"lstplayers {lstplayers}")  # Output: ['apple', 'banana', 'cherry']
cpplayers = players[:]
badcpplayers = players
players.append('gunter')

print(players[0:3])
print(players[-3:])
print(f"CPPLAYERS {cpplayers}")
print(f"BADCPLAYERS {badcpplayers}")
print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())
for play in tplayers:
    print(play)    