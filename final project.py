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

def update_draw_pile():
    global draw_pile_label, draw_pile
    draw_pile_label.config(text=f"Draw Pile: {len(draw_pile)}")


def update_discard_pile():
    global discard_pile_label
    if discard_pile:
        top_card = discard_pile[-1]
        card_image = card_images[top_card]
        discard_text = f"Current Game Card: {top_card}"
        discard_pile_label.config(image=card_image, text=discard_text)
        discard_pile_label.image = card_image
        discard_pile_label.config(text="Current Game Card")


def initialize_piles():
    global draw_pile, discard_pile
    draw_pile = list(deck)
    random.shuffle(draw_pile)
    discard_pile = [draw_pile.pop()]

    update_draw_pile()
    update_discard_pile()

card_images = {}

for color in colors:
    for number in numbers[1:]:
        image_path = f"/Users/josephinechen/PycharmProjects/CLPS0950-Final-Project/CLPS950_FinalProject_Cards/{number}{color}.png"
        card_image = Image.open(image_path)
        card_image = card_image.resize((100, 140))
        card_images[f"{number}{color}"] = ImageTk.PhotoImage(card_image)

    for action_card in action_cards:
        image_path = f"/Users/josephinechen/PycharmProjects/CLPS0950-Final-Project/CLPS950_FinalProject_Cards/{action_card}{color}.png"
        card_image = Image.open(image_path)
        card_image = card_image.resize((100, 140))
        card_images[f"{action_card}{color}"] = ImageTk.PhotoImage(card_image)

    for wild_card in wild_cards:
        image_path = f"/Users/josephinechen/PycharmProjects/CLPS0950-Final-Project/CLPS950_FinalProject_Cards/{wild_card}.png"
        card_image = Image.open(image_path)
        card_image = card_image.resize((100, 140))
        card_images[f"{wild_card}"] = ImageTk.PhotoImage(card_image)


def draw_random_card():
    global draw_pile, discard_pile, card_images

    if draw_pile:
        random_card = random.choice(draw_pile)
        card_image = card_images[random_card]

        random_card_label = tk.Label(window, image=card_image)
        random_card_label.pack()

        random_card_name_label = tk.Label(window, text=random_card)
        random_card_name_label.pack()



draw_pile_label = tk.Label(window, text="Draw Pile:")
draw_pile_label.pack()
discard_pile_label = tk.Label(window, text="Current Game Card:")
discard_pile_label.pack()


def deal_cards():
    global number_players, player_decks, deck
    number_players = int(number_players_var.get())
    player_decks = [[] for _ in range(number_players)]
    initialize_piles()

    for i in range(7):
        for j in range(number_players):
            if deck:
                player_decks[j].append(deck.pop())
            else:
                deck = list(discard_pile)
                random.shuffle(deck)
                discard_pile.clear()
                player_decks[j].append(deck.pop())

    start_option.destroy()
    number_players_label.destroy()
    number_players_dropdown.destroy()

    # Display the player's hand in the GUI
    for i in range(number_players):
        player_frame = tk.Frame(window)
        player_frame.pack()
        player_label = tk.Label(player_frame, text=f"Player {i+1}'s hand:")
        player_label.pack(side="left")

        for card in player_decks[i]:
            card_image = card_images[card]
            card_label = tk.Label(player_frame, image=card_image)
            card_label.pack(side="left")

    window.update()

    turn_window = tk.Toplevel(window)
    turn_window.title("Player Turn")
    starting_player = random.randint(1, number_players)
    starting_player_label = tk.Label(turn_window, text=f"Player {starting_player} can start!")
    starting_player_label.pack()
    window.after(3000, draw_random_card)
    turn_window.after(3000, starting_player_label.destroy)
    turn_window.after(3000,turn_window.destroy)

def customize_rules():
    global allow_stacking, force_play, rules_window
    rules_window = tk.Toplevel(window)

    allow_stacking_var = tk.StringVar(rules_window, "yes")
    allow_stacking_label = tk.Label(rules_window, text="Allow Stacking of Draw2 and Draw4 Cards?")
    allow_stacking_dropdown = tk.OptionMenu(rules_window, allow_stacking_var, "yes", "no")
    allow_stacking_label.pack(side="left")
    allow_stacking_dropdown.pack(side="left")

    force_play_var = tk.StringVar(rules_window, "yes")
    force_play_label = tk.Label(rules_window, text="Force Players to Play if they have a Playable Card?")
    force_play_dropdown = tk.OptionMenu(rules_window, force_play_var, "yes", "no")
    force_play_label.pack(side="left")
    force_play_dropdown.pack(side="left")

    allow_stacking = False

    def save_rules():
        global allow_stacking, force_play
        allow_stacking = allow_stacking_var.get() == "yes"
        force_play = force_play_var.get() == "yes"
        rules_window.destroy()
        deal_cards()

    save_button = tk.Button(rules_window, text="Save", command=save_rules)
    save_button.pack()

    rules_window.mainloop()


def quit_game():
    window.destroy()

def select_number_players():
    global number_players
    number_players = int(number_players_var.get())
    if number_players == 1:
        ai_label = tk.Label(window, text = "Playing Against AI")
        ai_label.pack()
    elif number_players in range(2,6):
        customize_rules()
    deal_cards()

start_option = tk.Button(window,text="Start Game", command=select_number_players)
start_option.pack()

window.mainloop()