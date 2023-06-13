#dependencies
import numpy as np
import matplotlib.pyplot as plt

#functions
def split_deck(deck):
    deck1 = deck[0:len(deck)//2]
    deck2 = deck[len(deck)//2:]
    return deck1, deck2

def riffle_shuffle(deck, deck1, deck2):
    shuffled = np.zeros_like(deck)
    for i in range(len(deck2)):
        shuffled[2*i] = deck1[i]
        shuffled[2*i+1] = deck2[i]
    return shuffled

#main function
x = int(input("Enter max deck numbers you want to find up to:"))

deck_sizes = []
riffle_counts = []

for i in range(2,x+2,2):
    deck_num = i
    deck = np.arange(1,deck_num+1,1)

    deck1, deck2 = split_deck(deck)
    shuffled = riffle_shuffle(deck, deck1, deck2)
    count = 1
    if ((shuffled == deck).all()):
        print(i, count)
        continue
    while(count > 0):
        deck1, deck2 = split_deck(shuffled)
        shuffled = riffle_shuffle(shuffled,deck1,deck2)
        count += 1
        if((shuffled==deck).all()):
            break
    print(i, count) #output corresponding deck size and number of riffle shuffles to return original position
    deck_sizes.append(i)
    riffle_counts.append(count)

x = np.linspace(0, x)
y = x/2
y2 = x/2

plt.plot(x, x, label='x=y')
plt.plot(x, y, label='x=1/2*y')
plt.plot(x, y2, label='x=1/3*y')

# Plotting
plt.scatter(deck_sizes, riffle_counts, marker='o', label="Data points")
plt.xlabel('Deck Size')
plt.ylabel('Number of Riffle Shuffles')
plt.title('Number of Riffle Shuffles Required for Different Deck Sizes')
plt.show()
plt.legend()