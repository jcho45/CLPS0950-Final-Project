import random
import tkinter as tk
from PIL import Image, ImageTk
import easygui


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
        self.players = []
        self.selected_color = None
        self.top_card = []
        self.reverse = False

        self.window = tk.Tk()
        self.window.title("UNAS AMIGAS")

        self.number_players_var = tk.StringVar(self.window, "2")
        self.number_players_label = tk.Label(self.window, text="Number of Players:")
        self.number_players_dropdown = tk.OptionMenu(self.window, self.number_players_var, "2", "3", "4", "5")
        self.number_players_label.pack(side="left")
        self.number_players_dropdown.pack(side="left")

        self.start_option = tk.Button(self.window, text="Start Game", command=self.select_number_players)
        self.start_option.pack()
        self.card_images = {}

        for color in self.colors:
            for number in self.numbers:
                image_path = f"/Users/josephinechen/PycharmProjects/CLPS0950-Final-Project/CLPS950_FinalProject_Cards/{number}{color}.png"
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

    def play_reverse_card(self):
        self.reverse = not self.reverse
        if self.reverse:
            self.player_turn_label.config(text=f"Player {self.current_player}'s turn (REVERSE)")
        else:
            self.player_turn_label.config(text=f"Player {self.current_player}'s turn")

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

            # Deal 7 cards to each player (excluding cards starting with "8")
            cards_to_deal = 7
            if i == 0:
                cards_to_deal -= 1  # Subtract an extra card for the first player
            for _ in range(cards_to_deal):
                while True:
                    card = self.draw_pile.pop()
                    if not card.startswith("8"):
                        break
                    else:
                        self.draw_pile.insert(0, card)  # Put the card back at the bottom of the draw pile
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

        # Draw the first card and check if it is an action or wild card
        first_card = self.draw_pile[0]
        while first_card.startswith(
                ("draw2", "skip", "reverse", "wild", "wild4", "8blue", "8green", "8red", "8yellow")):
            random.shuffle(self.draw_pile)
            first_card = self.draw_pile[0]

        self.draw_pile_label = tk.Label(self.window)
        self.discard_pile_label = tk.Label(self.window)
        self.player_turn_label = tk.Label(self.window, text=f"Player 1's turn")
        self.player_turn_label.pack()
        self.draw_pile_label.pack()
        self.discard_pile_label.pack()

        self.discard_pile = [self.draw_pile.pop(0)]
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
        self.play_button = tk.Button(self.window, text="Play Card",
                                     command=lambda: self.play_card(self.player_decks[self.current_player - 1],
                                                                    self.current_player, self.discard_pile, self.deck,
                                                                    self.players))
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

    def ask_for_color_selection(self):
        # create a new window
        window = tk.Toplevel()
        window.title("Color Selection")
        window.geometry("300x200")

        # create a label for instructions
        instructions_label = tk.Label(window, text="Please select a color:")
        instructions_label.pack(pady=10)

        # create buttons for each color option
        red_button = tk.Button(window, text="Red", bg="red", command=lambda: select_color("red"))
        red_button.pack(pady=5)
        green_button = tk.Button(window, text="Green", bg="green", command=lambda: select_color("green"))
        green_button.pack(pady=5)
        blue_button = tk.Button(window, text="Blue", bg="blue", command=lambda: select_color("blue"))
        blue_button.pack(pady=5)
        yellow_button = tk.Button(window, text="Yellow", bg="yellow", command=lambda: select_color("yellow"))
        yellow_button.pack(pady=5)

        # function to set the selected color and close the window
        def select_color(color):
            self.selected_color = color
            window.destroy()

        # initialize the selected color to None
        self.selected_color = None

        # run the window until it is closed
        window.grab_set()
        window.wait_window()
        return self.selected_color

    def play_card(self, player_deck, player, discard_pile, deck, players, wild_card_color=None):
        top_card = self.discard_pile[-1]
        valid_cards = []

        # Check if any card matches the color or number of the top card
        for valid_card in player_deck:
            if valid_card[0] == top_card[0] or valid_card[1:] == top_card[1:]:
                valid_cards.append(valid_card)

        # Check if any draw2, reverse, or skip card matches the color of the top card
        for valid_card in player_deck:
            if valid_card.startswith("draw2") and valid_card[-1] == top_card[-1]:
                valid_cards.append(valid_card)
            elif valid_card.startswith("reverse") and valid_card[-1] == top_card[-1]:
                valid_cards.append(valid_card)
            elif valid_card.startswith("skip") and valid_card[-1] == top_card[-1]:
                valid_cards.append(valid_card)

        # Include any wild or wild4 card
        valid_cards.extend([card for card in player_deck if card.startswith("wild")])


        # Additional logic for top card starting with draw2, skip, or reverse
        if top_card.startswith(("draw2", "skip", "reverse")):
            for valid_card in player_deck:
                if (valid_card.startswith("wild") or valid_card[0] == top_card[0] or valid_card.startswith(top_card[:-1])):
                    valid_cards.append(valid_card)

        if not valid_cards:
            if self.window.winfo_exists():  # Check if the main window is still active
                no_card_window = tk.Toplevel(self.window)
                no_card_window.title("No playable cards")
                no_card_label = tk.Label(no_card_window, text="No playable cards: Draw Card")
                no_card_label.pack()
                self.window.after(2000, lambda: no_card_window.destroy())  # Close the window after 2 seconds
                no_card_window.mainloop()

        window = tk.Toplevel(self.window)
        window.title("Play Card")

        def add_to_pile(card):
            player_deck.remove(card)

            if card.startswith(("draw2", "reverse", "skip", "wild4")):
                # Perform the action based on the card type
                window.destroy()  # Close the card selection window

                if card.startswith("draw2"):
                    # Skip the next player and make them draw 2 cards
                    draw2_window = tk.Toplevel()
                    draw2_window.title("Draw 2 Cards")
                    label = tk.Label(draw2_window, text="Next Player, draw 2 cards and end your turn.")
                    label.pack()
                    draw2_window.after(2000, draw2_window.destroy)  # Close the window after 2 seconds

                elif card.startswith("wild4"):
                    wild4_window = tk.Toplevel()
                    wild4_window.title("Draw 4 Cards")
                    label = tk.Label(wild4_window, text="Next Player, draw 4 cards and end your turn.")
                    label.pack()
                    wild4_window.after(2000, wild4_window.destroy)  # Close the window after 2 seconds

                elif card.startswith("skip"):
                    skip_window = tk.Toplevel()
                    skip_window.title("Skip Turn")
                    label = tk.Label(skip_window, text="Next Player, end your turn.")
                    label.pack()
                    skip_window.after(2000, skip_window.destroy)  # Close the window after 2 seconds

                elif card.startswith("reverse"):
                    self.play_reverse_card()
                if not self.reverse:
                    self.current_player += 1
                else:
                    self.current_player -= 1
                    if self.current_player == 0:
                        self.current_player = self.number_players

            if card.startswith("wild"):
                self.ask_for_color_selection()
                new_color = self.selected_color
                new_card = "8" + new_color
                self.discard_pile.append(new_card)
            else:
                self.discard_pile.append(card)

            self.update_discard_pile()
            window.destroy()

            for widget in self.player_frames[self.current_player - 1].winfo_children():
                widget.destroy()

            for card in player_deck:
                card_image = self.card_images[card]
                card_label = tk.Label(self.player_frames[self.current_player - 1], image=card_image)
                card_label.pack(side="left")

        for valid_card in valid_cards:
            card_image = self.card_images[valid_card]
            card_button = tk.Button(window, image=card_image, command=lambda c=valid_card: add_to_pile(c))
            card_button.pack(side="left", padx=5)

        window.mainloop()

        return None  # Player closed the window without selecting a card

    def show_winner_message(self, message):
        winner_window = tk.Toplevel(self.window)
        winner_window.title("Game Over")
        winner_label = tk.Label(winner_window, text=message)
        winner_label.pack()
        winner_window.after(2000, winner_window.destroy)

    def play_turn(self):
        player_deck = self.player_decks[self.current_player - 1]
        card_to_play = self.play_card(player_deck)
        if card_to_play is None:
            return False  # Player didn't play a card

        if len(player_deck) == 0:
            self.show_winner_message(f"Player {self.current_player} has no more cards. Game over!")
            return False

        player_deck.remove(card_to_play)
        self.discard_pile.append(card_to_play)
        self.update_discard_pile()
        self.update_draw_pile()

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
