import random 

# list of all 52 cards  
deck = []
# list that stores 13 random cards 
random_set = []


# list fo all cards and push to deck  
for i in range(4):
    for j in range(1, 14):
        deck.append([i, j])

# print deck
# print(deck, '\n')

for i in range(13):
    random_index = random.randint(0, len(deck) - 1)

    random_set.append(deck[random_index])
    deck.remove(deck[random_index])

print(random_set)

