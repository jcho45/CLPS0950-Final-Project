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

def customize_rules():
    global allow_stacking, force_play
    allow_stacking_var = tk.StringVar(window, "yes")
    allow_stacking_label = tk.Label(window, text="Allow Stacking of Draw2 and Draw4 Cards?")
    allow_stacking_dropdown = tk.OptionMenu(window, allow_stacking_var, "yes", "no")
    allow_stacking_label.pack(side="left")
    allow_stacking_dropdown.pack(side="left")

    force_play_var = tk.StringVar(window, "yes")
    force_play_label = tk.Label(window, text="Force Players to Play if they have a Playable Card?")
    force_play_dropdown = tk.OptionMenu(window, force_play_var, "yes", "no")
    force_play_label.pack(side="left")
    force_play_dropdown.pack(side="left")

    def save_rules():
        nonlocal allow_stacking, force_play
        allow_stacking = allow_stacking_var.get() == "yes"
        force_play = force_play_var.get() == "yes"
        rules_window.destroy()

    save_button = tk.Button(rules_window, text="Save", command=save_rules)
    save_button.pack()

    rules_window.mainloop()

def deal_cards():
    global number_players, player_decks, deck
    number_players = int(number_players_var.get())
    player_decks = [[] for _ in range(number_players)]

    for i in range(7):
        for j in range(number_players):
            if deck:
                player_decks[j].append(deck.pop())
            else:
                deck = list(discard_pile)
                random.shuffle(deck)
                discard_pile.clear()
                player_decks[j].append(deck.pop())

def quit_game():
    window.destroy()

def select_number_players():
    number_players = int(number_players_var.get())
    if number_players == 1:
        ai_label = tk.Label(window, text = "Playing Against AI")
        ai_label.pack()
    elif number_players in range(2,6):
        customize_rules()
        deal_cards()

window.mainloop()










