import random
def sfuffle_cards():
    shuffled_cards=[]
    deck=['2','3','4','5','6','7','8','9','10','K','Q','J','A']*4
    while deck:
        cards=deck.pop(random.randint(0,len(deck)-1))
        shuffled_cards.append(cards)
    print("Shuffled cards are: ",shuffled_cards)
sfuffle_cards()        