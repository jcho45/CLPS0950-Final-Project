import random
import tkinter as tk

colors = ["red", "yellow", "green", "blue"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
action_cards = ["skip", "reverse", "draw two"]
wild_cards = ["wild", "wild draw four"]

deck = []
for color_type in colors:
   for number_type in numers[1:]:
       deck.append(str(number_type)+""+color_type)
    for action_card_type in action_cards:
        deck.append(action_card_type +""+color_type)
    for wild_card_type in wild_cards:
        deck.append(wild_card_type)

random.shuffle(deck)


