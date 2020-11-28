from random import shuffle

SUITE = "H D S C".split()
RANKS = '2 3 4 5 6 7 8 9 10 K Q K A'.split()



class Deck:
    def __init__(self):
        print("CREATINIG NEW DECK")
        self.allcards = [(s,r) for s in SUITE for r in RANKS]

    def shuffle(self):
        print("SHUFFLING DECK")
        shuffle(self.allcards)
    
    def split_in_half(self):
        print("SPLITTING IN HALF")
        return(self.allcards[:26], self.allcards[26:])
class Hand:
    def __init__(self, cards):
        self.cards = cards
    
    def __str__(self):
        return "contains {} cards".format(len(self.cards))
    
    def add(self, added_cards):
        self.cards.extend(added_cards)

    def remove_card(self):
        return self.cards.pop()

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand
    
    def play_card(self):
        drawn_card = self.hand.remove_card()
        print("{} has placed {}".format(self.name, drawn_card))
        print("")
        return drawn_card
    
    def remove_war_cards(self):
        war_cards = []
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.cards.pop())
            return war_cards

    def still_has_cards(self):
        return len(self.hand.cards) != 0

print("Welcome to war, let's begin")


d = Deck()
d.shuffle()
half1, half2 = d.split_in_half()

com = Player("computer", Hand(half1))

name = input("What's your name?")
user = Player(name, Hand(half2))


total_rounds = 0
war_count = 0
while user.still_has_cards() and com.still_has_cards():
    total_rounds += 1
    print("NEW ROUND")
    print("Current standings!: ")
    print(user.name + " has the count: "+str(len(user.hand.cards)))
    print(com.name + " has the count: "+str(len(com.hand.cards)))

    table_cards = []

    c_card = com.play_card()
    p_card = user.play_card()

    table_cards.append(c_card)
    table_cards.append(p_card)

    if c_card[1] == p_card[1]:
        war_count += 1

        print("WAR")

        table_cards.extend(user.remove_war_cards())
        table_cards.extend(com.remove_war_cards())

        # Play cards
        c_card = com.play_card()
        p_card = user.play_card()

        # Add to table_cards
        table_cards.append(c_card)
        table_cards.append(p_card)

        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            com.hand.add(table_cards)
    else:
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            user.hand.add(table_cards)
        else:
            com.hand.add(table_cards)

print("GAme over, number of rounds: "+str(total_rounds))
print("A war happened "+str(war_count)+" times")
print("Does the computer still have cards?")
print(str(com.still_has_cards()))
print("Does the user still have cards?")
print(str(user.still_has_cards()))