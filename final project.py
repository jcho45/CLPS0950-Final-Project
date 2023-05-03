import random
import tkinter as tk

colors = ["red", "yellow", "green", "blue"]
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
action_cards = ["skip", "reverse", "draw two"]
wild_cards = ["wild", "wild draw four"]
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
number_players_label = tk.Label(root, text="Number of Players:")
number_players_dropdown = tk.OptionMenu(window, number_player_var, "1","2","3","4","5")
number_players_label.pack(side="left")
number_players_dropdown.pack(side="left")

card_png = {}

for n in colors:
    for iter in numbers[1:]:
        image_loc = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/b_0.png"
        card_png = image.open(image_loc)
        card_png = card_png.resize((100,150))
        card_images[f"{zero}_{blue}"]=ImageTk.PhotoImage(card_png)

        image_loc_1 = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/b_1.png"
        card_png_1 = image.open(image_loc_1)
        card_png_1 = card_png_1.resize((100,150))
        card_images_1[f"{one}_{blue}"]=ImageTk.PhotoImage(card_png_1)

        image_loc_2 = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/b_2.png"
        card_png_2 = image.open(image_loc_2)
        card_png_2 = card_png_2.resize((100, 150))
        card_images_2[f"{two}_{blue}"] = ImageTk.PhotoImage(card_png_2)

        image_loc_3 = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/b_3.png"
        card_png_3 = image.open(image_loc_3)
        card_png_3 = card_png_3.resize((100, 150))
        card_images_3[f"{three}_{blue}"] = ImageTk.PhotoImage(card_png_3)

        image_loc_4 = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/b_4.png"
        card_png_4 = image.open(image_loc_4)
        card_png_4 = card_png_4.resize((100, 150))
        card_images_4[f"{four}_{blue}"] = ImageTk.PhotoImage(card_png_4)

        image_loc_5 = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/b_5.png"
        card_png_5 = image.open(image_loc_5)
        card_png_5 = card_png_5.resize((100, 150))
        card_images_5[f"{five}_{blue}"] = ImageTk.PhotoImage(card_png_5)

        image_loc_6 = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/b_6.png"
        card_png_6 = image.open(image_loc_6)
        card_png_6 = card_png_6.resize((100, 150))
        card_images_6[f"{six}_{blue}"] = ImageTk.PhotoImage(card_png_6)

        image_loc_7 = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/b_7.png"
        card_png_7 = image.open(image_loc_7)
        card_png_7 = card_png_7.resize((100, 150))
        card_images_7[f"{seven}_{blue}"] = ImageTk.PhotoImage(card_png_7)

        image_loc_8 = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/b_8.png"
        card_png_8 = image.open(image_loc_8)
        card_png_8 = card_png_8.resize((100, 150))
        card_images_8[f"{eight}_{blue}"] = ImageTk.PhotoImage(card_png_8)

        image_loc_9 = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/b_9.png"
        card_png_9 = image.open(image_loc_9)
        card_png_9 = card_png_9.resize((100, 150))
        card_images_9[f"{nine}_{blue}"] = ImageTk.PhotoImage(card_png_9)

        image_loc_p2 = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/b_p2.png"
        card_png_p2 = image.open(image_loc_p2)
        card_png_p2 = card_png_p2.resize((100, 150))
        card_images_p2[f"{plus 2}_{blue}"] = ImageTk.PhotoImage(card_png_p2)

        image_loc_reverse = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/b_reverse.png"
        card_png_reverse = image.open(image_loc_reverse)
        card_png_reverse = card_png_reverse.resize((100, 150))
        card_images_reverse[f"{reverse}_{blue}"] = ImageTk.PhotoImage(card_png_reverse)

        image_loc_skip = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/b_skip.png"
        card_png_skip = image.open(image_loc_skip)
        card_png_skip = card_png_skip.resize((100, 150))
        card_images_skip[f"{skip}_{blue}"] = ImageTk.PhotoImage(card_png_skip)

        image_loc_g = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/g_0.png"
        card_png_g = image.open(image_loc_g)
        card_png_g = card_png_g.resize((100, 150))
        card_images_g[f"{zero}_{green}"] = ImageTk.PhotoImage(card_png_g)

        image_loc_1_g = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/g_1.png"
        card_png_1_g = image.open(image_loc_1_g)
        card_png_1_g = card_png_1_g.resize((100, 150))
        card_images_1_g[f"{one}_{green}"] = ImageTk.PhotoImage(card_png_1_g)

        image_loc_2_g = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/g_2.png"
        card_png_2_g = image.open(image_loc_2_g)
        card_png_2_g = card_png_2_g.resize((100, 150))
        card_images_2_g[f"{two}_{green}"] = ImageTk.PhotoImage(card_png_2_g)

        image_loc_3_g = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/g_3.png"
        card_png_3_g = image.open(image_loc_3_g)
        card_png_3_g = card_png_3_g.resize((100, 150))
        card_images_3_g[f"{three}_{green}"] = ImageTk.PhotoImage(card_png_3_g)

        image_loc_4_g = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/g_4.png"
        card_png_4_g = image.open(image_loc_4_g)
        card_png_4_g = card_png_4_g.resize((100, 150))
        card_images_4_g[f"{four}_{green}"] = ImageTk.PhotoImage(card_png_4_g)

        image_loc_5_g = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/g_5.png"
        card_png_5_g = image.open(image_loc_5_g)
        card_png_5_g= card_png_5_g.resize((100, 150))
        card_images_5_g[f"{five}_{green}"] = ImageTk.PhotoImage(card_png_5_g)

        image_loc_6_g = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/g_6.png"
        card_png_6_g = image.open(image_loc_6_g)
        card_png_6_g = card_png_6_g.resize((100, 150))
        card_images_6_g[f"{six}_{green}"] = ImageTk.PhotoImage(card_png_6_g)

        image_loc_7_g = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/g_7.png"
        card_png_7_g = image.open(image_loc_7_g)
        card_png_7_g = card_png_7_g.resize((100, 150))
        card_images_7_g[f"{seven}_{green}"] = ImageTk.PhotoImage(card_png_7_g)

        image_loc_8_g = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/g_8.png"
        card_png_8_g = image.open(image_loc_8_g)
        card_png_8_g = card_png_8_g.resize((100, 150))
        card_images_8_g[f"{eight}_{green}"] = ImageTk.PhotoImage(card_png_8_g)

        image_loc_9_g = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/g_9.png"
        card_png_9_g = image.open(image_loc_9_g)
        card_png_9_g = card_png_9_g.resize((100, 150))
        card_images_9_g[f"{nine}_{green}"] = ImageTk.PhotoImage(card_png_9_g)

        image_loc_p2_g = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/g_p2.png"
        card_png_p2_g = image.open(image_loc_p2_g)
        card_png_p2_g = card_png_p2_g.resize((100, 150))
        card_images_p2_g[f"{plus 2}_{green}"] = ImageTk.PhotoImage(card_png_p2_g)

        image_loc_reverse_g = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/g_reverse.png"
        card_png_reverse_g = image.open(image_loc_reverse_g)
        card_png_reverse_g = card_png_reverse_g.resize((100, 150))
        card_images_reverse_g[f"{reverse}_{green}"] = ImageTk.PhotoImage(card_png_reverse_g)

        image_loc_skip_g = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/g_skip.png"
        card_png_skip_g = image.open(image_loc_skip_g)
        card_png_skip_g = card_png_skip_g.resize((100, 150))
        card_images_skip_g[f"{skip}_{green}"] = ImageTk.PhotoImage(card_png_skip_g)

        image_loc_y = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/y_0.png"
        card_png_y = image.open(image_loc_y)
        card_png_y = card_png_y.resize((100, 150))
        card_images_y[f"{zero}_{yellow}"] = ImageTk.PhotoImage(card_png_y)

        image_loc_1_y = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/y_1.png"
        card_png_1_y = image.open(image_loc_1_y)
        card_png_1_y = card_png_1_y.resize((100, 150))
        card_images_1_y[f"{one}_{yellow}"] = ImageTk.PhotoImage(card_png_1_y)

        image_loc_2_y = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/y_2.png"
        card_png_2_y = image.open(image_loc_2_y)
        card_png_2_y = card_png_2_y.resize((100, 150))
        card_images_2_y[f"{two}_{yellow}"] = ImageTk.PhotoImage(card_png_2_y)

        image_loc_3_y = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/y_3.png"
        card_png_3_y = image.open(image_loc_3_y)
        card_png_3_y = card_png_3_y.resize((100, 150))
        card_images_3_y[f"{three}_{yellow}"] = ImageTk.PhotoImage(card_png_3_y)

        image_loc_4_y = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/y_4.png"
        card_png_4_y = image.open(image_loc_4_y)
        card_png_4_y = card_png_4_y.resize((100, 150))
        card_images_4_y[f"{four}_{yellow}"] = ImageTk.PhotoImage(card_png_4_y)

        image_loc_5_y = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/y_5.png"
        card_png_5_y = image.open(image_loc_5_y)
        card_png_5_y = card_png_5_y.resize((100, 150))
        card_images_5_y[f"{five}_{yellow}"] = ImageTk.PhotoImage(card_png_5_y)

        image_loc_6_y = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/y_6.png"
        card_png_6_y = image.open(image_loc_6_y)
        card_png_6_y = card_png_6_y.resize((100, 150))
        card_images_6_y[f"{six}_{yellow}"] = ImageTk.PhotoImage(card_png_6_y)

        image_loc_7_y = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/y_7.png"
        card_png_7_y = image.open(image_loc_7_y)
        card_png_7_y = card_png_7_y.resize((100, 150))
        card_images_7_y[f"{seven}_{yellow}"] = ImageTk.PhotoImage(card_png_7_y)

        image_loc_8_y = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/y_8.png"
        card_png_8_y = image.open(image_loc_8_y)
        card_png_8_y = card_png_8_y.resize((100, 150))
        card_images_8_y[f"{eight}_{yellow}"] = ImageTk.PhotoImage(card_png_8_y)

        image_loc_9_y = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/y_9.png"
        card_png_9_y = image.open(image_loc_9_y)
        card_png_9_y = card_png_9_y.resize((100, 150))
        card_images_9_y[f"{nine}_{yellow}"] = ImageTk.PhotoImage(card_png_9_y)

        image_loc_p2_y = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/y_p2.png"
        card_png_p2_y = image.open(image_loc_p2_y)
        card_png_p2_y = card_png_p2_y.resize((100, 150))
        card_images_p2_y[f"{plus 2}_{yellow}"] = ImageTk.PhotoImage(card_png_p2_y)

        image_loc_reverse_y = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/y_reverse.png"
        card_png_reverse_y = image.open(image_loc_reverse_y)
        card_png_reverse_y = card_png_reverse_y.resize((100, 150))
        card_images_reverse_y[f"{reverse}_{yellow}"] = ImageTk.PhotoImage(card_png_reverse_y)

        image_loc_skip_y = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/y_skip.png"
        card_png_skip_y = image.open(image_loc_skip_y)
        card_png_skip_y = card_png_skip_y.resize((100, 150))
        card_images_skip_y[f"{skip}_{yellow}"] = ImageTk.PhotoImage(card_png_skip_y)

        image_loc_r = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/r_0.png"
        card_png_r = image.open(image_loc_r)
        card_png_r = card_png_r.resize((100, 150))
        card_images_r[f"{zero}_{red}"] = ImageTk.PhotoImage(card_png_r)

        image_loc_1_r = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/r_1.png"
        card_png_1_r = image.open(image_loc_1_r)
        card_png_1_r = card_png_1_r.resize((100, 150))
        card_images_1_r[f"{one}_{red}"] = ImageTk.PhotoImage(card_png_1_r)

        image_loc_2_r = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/r_2.png"
        card_png_2_r = image.open(image_loc_2_r)
        card_png_2_r = card_png_2_r.resize((100, 150))
        card_images_2_r[f"{two}_{red}"] = ImageTk.PhotoImage(card_png_2_r)

        image_loc_3_r = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/r_3.png"
        card_png_3_r = image.open(image_loc_3_r)
        card_png_3_r = card_png_3_r.resize((100, 150))
        card_images_3_r[f"{three}_{red}"] = ImageTk.PhotoImage(card_png_3_r)

        image_loc_4_r = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/r_4.png"
        card_png_4_r = image.open(image_loc_4_r)
        card_png_4_r = card_png_4_r.resize((100, 150))
        card_images_4_r[f"{four}_{red}"] = ImageTk.PhotoImage(card_png_4_r)

        image_loc_5_r = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/r_5.png"
        card_png_5_r = image.open(image_loc_5_r)
        card_png_5_r = card_png_5_r.resize((100, 150))
        card_images_5_r[f"{five}_{red}"] = ImageTk.PhotoImage(card_png_5_r)

        image_loc_6_r = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/r_6.png"
        card_png_6_r = image.open(image_loc_6_r)
        card_png_6_r = card_png_6_r.resize((100, 150))
        card_images_6_r[f"{six}_{red}"] = ImageTk.PhotoImage(card_png_6_r)

        image_loc_7_r = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/r_7.png"
        card_png_7_r = image.open(image_loc_7_r)
        card_png_7_r = card_png_7_r.resize((100, 150))
        card_images_7_r[f"{seven}_{red}"] = ImageTk.PhotoImage(card_png_7_r)

        image_loc_8_r = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/r_8.png"
        card_png_8_r = image.open(image_loc_8_r)
        card_png_8_r = card_png_8_r.resize((100, 150))
        card_images_8_r[f"{eight}_{red}"] = ImageTk.PhotoImage(card_png_8_r)

        image_loc_9_r = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/r_9.png"
        card_png_9_r = image.open(image_loc_9_r)
        card_png_9_r = card_png_9_r.resize((100, 150))
        card_images_9_r[f"{nine}_{red}"] = ImageTk.PhotoImage(card_png_9_r)

        image_loc_p2_r = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/r_p2.png"
        card_png_p2_r = image.open(image_loc_p2_r)
        card_png_p2_r = card_png_p2_r.resize((100, 150))
        card_images_p2_r[f"{plus 2}_{red}"] = ImageTk.PhotoImage(card_png_p2_r)

        image_loc_reverse_r = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/r_reverse.png"
        card_png_reverse_r = image.open(image_loc_reverse_r)
        card_png_reverse_r = card_png_reverse_r.resize((100, 150))
        card_images_reverse_r[f"{reverse}_{red}"] = ImageTk.PhotoImage(card_png_reverse_r)

        image_loc_skip_r = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/r_skip.png"
        card_png_skip_r = image.open(image_loc_skip_r)
        card_png_skip_r = card_png_skip_r.resize((100, 150))
        card_images_skip_r[f"{skip}_{red}"] = ImageTk.PhotoImage(card_png_skip_r)

        image_loc_wild = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/wild.png"
        card_png_wild = image.open(image_loc_wild)
        card_png_wild = card_png_wild.resize((100, 150))
        card_images_wild[f"{wild}_{wild}"] = ImageTk.PhotoImage(card_png_wild)

        image_loc_wild_2 = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/wild_2.png"
        card_png_wild_2 = image.open(image_loc_wild_2)
        card_png_wild_2 = card_png_wild_2.resize((100, 150))
        card_images_wild_2[f"{wild_2}_{wild_2}"] = ImageTk.PhotoImage(card_png_wild_2)

        image_loc_wild_p4 = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/wild_p4.png"
        card_png_wild_p4 = image.open(image_loc_wild_p4)
        card_png_wild_p4 = card_png_wild_p4.resize((100, 150))
        card_images_wild_p4[f"{wild_p4}_{wild_p4}"] = ImageTk.PhotoImage(card_png_wild_p4)

        image_loc_wild_p4_2 = f"/Users/josephinechen/Documents/2022-23 SPRING /CLPS950_FinalProject_Cards/wild_p4_2.png"
        card_png_wild_p4_2 = image.open(image_loc_wild_p4_2)
        card_png_wild_p4_2 = card_png_wild_p4_2.resize((100, 150))
        card_images_wild_p4_2[f"{wild_p4_2}_{wild_p4_2}"] = ImageTk.PhotoImage(card_png_wild_p4_2)

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
        ai_label = tk.Label(window, f text = "Playing Against AI")
        ai_label.pack()
    elif number_players in range(2,6):
        deal_cards()












