import random 

# list of all 52 cards  
deck = []
# list that stores 13 random cards 
random_set = []


# list fo all cards and push to deck  
for i in range(4):
    for j in range(1, 14):
        deck.append([i, j])


# DECK = {[SYMBOL, A TO K]}

# print deck
# print(deck, '\n')

for i in range(13):
    random_index = random.randint(0, len(deck) - 1)
    random_set.append(deck[random_index])
    deck.remove(deck[random_index])

print(random_set, '\n\n')

# fuction returns similar number but not the symbols
def find_same_number(s):
    return_list = []
    for card in s:
        t = []
        for x in s:
            if (card[1] == x[1]):
                t.append(card)
                t.append(x)
        return_list.append(t)
    return return_list

for i in find_same_number(random_set):
    print(i)