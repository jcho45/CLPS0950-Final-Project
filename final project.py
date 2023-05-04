import random
import tkinter as tk
from PIL import Image, ImageTk


colors = ["red", "yellow", "green", "blue"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
action_cards = ["skip", "reverse", "draw2"]
wild_cards = ["wild", "wild4"]
flipped_card = ["black"]

deck = []
for color_type in colors:
   for number_type in numbers[1:]:
       deck.append(str(number_type)+""+color_type)
   for action_card_type in action_cards:
        deck.append(action_card_type +""+color_type)
   for wild_card_type in wild_cards:
        deck.append(wild_card_type)

random.shuffle(deck)

player_decks = []
number_players = 1
draw_pile = []
discard_pile = []

window = tk.Tk()
window.title("UNAS AMIGAS")

number_players_var = tk.StringVar(window,"1")
number_players_label = tk.Label(window, text="Number of Players:")
number_players_dropdown = tk.OptionMenu(window, number_players_var, "1","2","3","4","5")
number_players_label.pack(side="left")
number_players_dropdown.pack(side="left")

card_images = {}

for color in colors:
    for number in numbers[1:]:
        image_path = f"/Users/josephinechen/PycharmProjects/pythonProject/CLPS950_FinalProject_Cards/{color}_{number}.png"
        card_image = Image.open(image_path)
        card_image = card_image.resize((100, 140))
        card_images[f"{number}_{color}"] = ImageTk.PhotoImage(card_image)

    for action_card in action_cards:
        image_path = f"/Users/josephinechen/PycharmProjects/pythonProject/CLPS950_FinalProject_Cards/{color}_{action_card}.png"
        card_image = Image.open(image_path)
        card_image = card_image.resize((100, 140))
        card_images[f"{action_card}_{color}"] = ImageTk.PhotoImage(card_image)

    for wild_card in wild_cards:
        image_path = f"/Users/josephinechen/PycharmProjects/pythonProject/CLPS950_FinalProject_Cards/{wild_card}.png"
        card_image = Image.open(image_path)
        card_image = card_image.resize((100, 140))
        card_images[wild_card] = ImageTk.PhotoImage(card_image)


def deal_cards():
    global number_players, player_decks, deck
    number_players = int(number_players_var.get())
    player_decks = [[] for _ in range(number_players)]

    for i in range(7):
        for j in range(number_players):
            player_decks[j].append(deck.pop())

def quit_game():
    window.destroy()

def select_number_players():
    number_players = int(number_players_var.get())
    if number_players == 1:
        ai_label = tk.Label(window, text = "Playing Against AI")
        ai_label.pack()
    elif number_players in range(2,6):
        deal_cards()

window.mainloop()










