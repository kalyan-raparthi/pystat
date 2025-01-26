# list fo all cards of single deck
import random 

deck = []
random_set = []


for i in range(4):
    for j in range(1, 14):
        deck.append([f"{i}", f"{j}"])

# print(deck, '\n')

for i in range(13):
    random_index = random.randint(0, len(deck) - 1)

    random_set.append(deck[random_index])
    deck.remove(deck[random_index])

# printing random distributed set 
for i in random_set: 
    print(i)

print('\n')
zero  = []
one   = []
two   = []
three = []

for i in random_set:
    # print(i[0])
    if (i[0] == '0'):
        zero.append(i)
    elif (i[0] == '1'):
        one.append(i)
    elif (i[0] == '2'):
        two.append(i)
    else :
        three.append(i)

print(zero)
print(one)
print(two)
print(three)

print('\nSET SIZE :', len(one) + len(two) + len(three) + len(zero))

same = []
for i in random_set:
    for n in range(13):
            for x in range(4):
                