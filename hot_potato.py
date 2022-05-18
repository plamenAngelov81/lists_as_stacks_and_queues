#players = ["aa", "bb", "cc", "dd", "ee", "ff", "gg", "hh", "ii", "jj", "kk"]
players = input().split()
step = int(input())
counter = 1

while len(players) > 1:
    name = players[0]
    if counter == step:
        players.remove(name)
        print(f"Removed {name}")
        counter = 0
    else:
        players.remove(name)
        players.append(name)
    counter += 1
else:
    print(f'Last is {"".join(players)}')
