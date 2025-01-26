# list fo all cards of single deck
deck = []

for i in range(4):
    for j in range(14):
        deck.append([f"{i}", f"{j}"])

for i in deck: 
    print(i)