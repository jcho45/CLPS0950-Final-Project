import random
import tkinter as tk
from PIL import Image, ImageTk

class UNOGame:
   def __init__(self):
       self.colors = ["red", "yellow", "green", "blue"]
       self.numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
       self.action_cards = ["skip", "reverse", "draw2"]
       self.wild_cards = ["wild", "wild4"]

       self.deck = []
       for color_type in self.colors:
           for number_type in self.numbers:
               self.deck.append(str(number_type) + "" + color_type)
           for action_card_type in self.action_cards:
               self.deck.append(action_card_type + "" + color_type)
       for wild_card_type in self.wild_cards:
           self.deck.append(wild_card_type)

       random.shuffle(self.deck)

       self.number_players = 1
       self.draw_pile = []
       self.discard_pile = []
       self.player_turn_label = None
       self.player_frames = []
       self.current_player = 1  # Variable to keep track of the current player's turn

       self.window = tk.Tk()
       self.window.title("UNAS AMIGAS")

       self.number_players_var = tk.StringVar(self.window, "1")
       self.number_players_label = tk.Label(self.window, text="Number of Players:")
       self.number_players_dropdown = tk.OptionMenu(self.window, self.number_players_var, "2", "3", "4", "5", "6")
       self.number_players_label.pack(side="left")
       self.number_players_dropdown.pack(side="left")

       self.start_option = tk.Button(self.window, text="Start Game", command=self.select_number_players)
       self.start_option.pack()
       self.card_images = {}

       for color in self.colors:
           for number in self.numbers:
               image_path = f"//Users/josephinechen/PycharmProjects/CLPS0950-Final-Project/CLPS950_FinalProject_Cards/{number}{color}.png"
               card_image = Image.open(image_path)
               card_image = card_image.resize((50, 70))
               self.card_images[f"{number}{color}"] = ImageTk.PhotoImage(card_image)

           for action_card in self.action_cards:
               image_path = f"/Users/josephinechen/PycharmProjects/CLPS0950-Final-Project/CLPS950_FinalProject_Cards/{action_card}{color}.png"
               card_image = Image.open(image_path)
               card_image = card_image.resize((50, 70))
               self.card_images[f"{action_card}{color}"] = ImageTk.PhotoImage(card_image)

       for wild_card in self.wild_cards:
           image_path = f"/Users/josephinechen/PycharmProjects/CLPS0950-Final-Project/CLPS950_FinalProject_Cards/{wild_card}.png"
           card_image = Image.open(image_path)
           card_image = card_image.resize((50, 70))
           self.card_images[f"{wild_card}"] = ImageTk.PhotoImage(card_image)

       self.window.mainloop()

   def deal_cards(self):
       self.player_decks = [[] for _ in range(self.number_players)]
       self.initialize_piles()

       self.draw_pile_label = tk.Label(self.window)
       self.update_draw_pile()
       self.draw_pile_label.pack()

       self.discard_pile_label = tk.Label(self.window)
       self.discard_pile_label.pack()

       self.player_labels = []

       for i in range(self.number_players):
           player_frame = tk.Frame(self.window)
           player_frame.pack()
           player_label = tk.Label(player_frame, text=f"Player {i + 1}'s hand:")
           player_label.pack(side="left")
           self.player_labels.append(player_label)

           # Deal 7 cards to each player
           cards_to_deal = 7
           if i == 0:
               cards_to_deal -= 1  # Subtract an extra card for the first player
           for _ in range(cards_to_deal):
               card = self.draw_pile.pop()
               self.player_decks[i].append(card)
               card_image = self.card_images[card]
               card_label = tk.Label(player_frame, image=card_image)
               card_label.pack(side="left")

           self.player_frames.append(player_frame)

       self.window.update()
       self.start()

   def initialize_piles(self):
       self.draw_pile = list(self.deck)
       random.shuffle(self.draw_pile)
       self.discard_pile = [self.draw_pile.pop()]

       self.player_turn_label = tk.Label(self.window, text=f"Player 1's turn")
       self.player_turn_label.pack()
       self.draw_pile_label = tk.Label(self.window)
       self.draw_pile_label.pack()
       self.discard_pile_label = tk.Label(self.window)
       self.discard_pile_label.pack()

       self.update_discard_pile()

   def update_discard_pile(self):
       if self.discard_pile:
           top_card = self.discard_pile[-1]
           card_image = self.card_images[top_card]
           self.discard_pile_label.config(image=card_image)
           self.discard_pile_label.image = card_image

   def start(self):
       self.draw_button = tk.Button(self.window, text="Draw", command=self.draw_random_card)
       self.draw_button.pack()
       self.draw_random_card()
       self.play_button = tk.Button(self.window, text="Play Card", command=lambda: self.play_card(self.player_decks[self.current_player-1]))
       self.play_button.pack()
       self.end_turn_button = tk.Button(self.window, text="End Turn", command=self.end_turn)
       self.end_turn_button.pack()

       # Hide all player frames except the current player's frame
       for i, frame in enumerate(self.player_frames):
           if i == self.current_player - 1:
               frame.pack()
           else:
               frame.pack_forget()

   def select_number_players(self):
       self.number_players = int(self.number_players_var.get())
       if self.number_players in range(2, 6):
           self.deal_cards()

       self.start_option.destroy()
       self.number_players_label.pack_forget()
       self.number_players_dropdown.pack_forget()

   def update_draw_pile(self):
       self.draw_pile_label.config()

   def draw_random_card(self):
       if self.draw_pile:
           random_card = random.choice(self.draw_pile)
           card_image = self.card_images[random_card]

           self.draw_pile.remove(random_card)
           self.update_draw_pile()

           self.player_decks[self.current_player - 1].append(random_card)
           card_label = tk.Label(self.player_frames[self.current_player - 1], image=card_image)
           card_label.pack(side="left")
       else:
           pass  # Handle case when draw pile is empty

   def play_card(self, player_deck):
       top_card = self.discard_pile[-1]
       valid_cards = [card for card in player_deck if card[0] == top_card[0] or card[1:] == top_card[1:]]
       if not valid_cards:
           return None  # No valid card to play

       window = tk.Toplevel(self.window)
       window.title("Play Card")

       card_labels = []
       for card in player_deck:
           if card in valid_cards:
               card_image = self.card_images[card]
           else:
               card_image = self.card_images["blank"]
           card_label = tk.Label(window, image=card_image)
           card_label.card = card
           card_label.bind("<Button-1>", lambda event: window.destroy())
           card_label.pack(side="left", padx=5)
           card_labels.append(card_label)

       window.wait_window()

       for card_label in card_labels:
           if hasattr(card_label, "selected") and card_label.selected:
               return card_label.card

       return None  # Player closed the window without selecting a card

   def play_turn(self):
       player_deck = self.player_decks[self.current_player - 1]
       card_to_play = self.play_card(player_deck)
       if card_to_play is None:
           return False  # Player didn't play a card

       player_deck.remove(card_to_play)
       self.discard_pile.append(card_to_play)
       self.update_discard_pile()
       self.update_draw_pile()

       # Handle special card effects here

       self.current_player = (self.current_player % self.number_players) + 1
       self.player_turn_label.config(text=f"Player {self.current_player}'s turn")
       return True

   def end_turn(self):
       self.current_player = (self.current_player % self.number_players) + 1
       self.player_turn_label.config(text=f"Player {self.current_player}'s turn")

       # Update the visibility of player frames
       for i, frame in enumerate(self.player_frames):
           if i == self.current_player - 1:
               frame.pack()
           else:
               frame.pack_forget()

if __name__ == "__main__":
   uno_game = UNOGame()