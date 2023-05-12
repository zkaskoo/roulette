import random
import time
from roulettelines import line_1, line_2, line_3

green = []
red = []
black = []
cont = input("Do you want to start the game?")
inp = int(input("Place here your money:"))
client = inp
bet = 0
bet_client = 0
bet_rounds = 0
bet_color = 0
bet_color_black = 0
bet_color_red = 0
quarters_1st = 0
quarters_2nd = 0
quarters_3rd = 0
bet_color_invest = 0
quarter_bet = 0
lines_bet = 0
while cont.upper() == 'YES':
    chose = input("Type what u want to play? color, quaters or lines?:")
    if chose.upper() == "COLOR":
        color = input("Type a color(red,black)")
        if color.upper() == "BLACK":
            bet_color = int(input("How much money you want to put in?:"))
            bet_color_black += bet_color
        if color.upper() == "RED":
            bet_color = int(input("How much money you want to put in?:"))
            bet_color_red += bet_color
    elif chose.upper() == "QUATERS":
        quarter = input("Do you want to bet the 1st 2nd or 3rd?\n Type 1st or 2nd or 3rd or skip")
        if quarter.upper() == "1ST":
            quarter_bet = int(input("How much money you want to put on the 1st quarter?:"))
            quarters_1st += quarter_bet
        if quarter.upper() == "2ND":
            quarter_bet = int(input("How much money you want to put on the 2nd quarter?:"))
            quarters_2nd += quarter_bet
        if quarter.upper() == "3RD":
            quarter_bet = int(input("How much money you want to put on the 3rd quarter?:"))
            quarters_3rd += quarter_bet
 #       if quarter.upper() != 'SKIP':
 #           quarter_bet = int(input("How much money you want to put on your picked quarter?:"))
    elif chose.upper() == "LINES":
        lines = input("Witch line you want to play?\n 1st or 2nd or 3rd or skip?")
        if lines.upper() != "SKIP":
            lines_bet = int(input("How much money you want to put on your picked line?:"))
    bet += bet_color
    bet += quarter_bet
    bet += lines_bet
    bet_rounds += bet_color
    bet_rounds += quarter_bet
    bet_rounds += lines_bet
    bet_client += bet_color
    bet_client += quarter_bet
    bet_client += lines_bet
    print(f'koronkenti bet {bet_rounds}')
    while bet_rounds > client:
        print("You cant bet more money then you have..!")
        bet = int(input("How much money you want to put in?:"))
    cont = input("Do you want to bet more?\n Yes or No?:")
    client -= bet_client
    bet_rounds = 0
    bet_client = 0
    if cont.upper() == "YES":
        continue
# seperate the numbers witch green,red or black

    for element in range(0, 11):
        if element == 0:
            green.append(element)
        elif element % 2 == 0 and element != 0:
            black.append(element)
        else:
            red.append(element)
    for element in range(11, 20):
        if element % 2 == 0:
            red.append(element)
        else:
            black.append(element)
    for element in range(20, 28):
        if element % 2 == 0:
            black.append(element)
        else:
            red.append(element)
    for element in range(28, 37):
        if element % 2 == 0:
            red.append(element)
        else:
            black.append(element)

# where the magic happens
# random picking a number between 0 and 36
    print('Throwing in progress.. please wait..')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(2)
    chosen = 0
    for element in range(1):
        chosen = random.randint(0, 36)
    if chosen in black:
        print(f'Black {chosen}')
    elif chosen in red:
        print(f'Red {chosen}')
    else:
        print(f'Green {chosen}')
    time.sleep(1)

# black or red mathematical calculaion
    if chose.upper() == "COLOR":
        if color == 'black' and chosen in black:
            print(f'Your balance is {client + bet_color_black*2}$')
            client += bet_color_black*2
        if color == 'black' and chosen not in black:
            print(f'Your balance is {client}$')
        if color == 'red' and chosen in red:
            print(f'Your balance is {client + bet_color_red*2}$')
            client += bet_color_red*2
            print(bet)
        if color == 'red' and chosen not in red:
            print(f'Your balance is {client}$')
            print(bet)
    bet_color_black = 0
    bet_color_red = 0
# quarters mathematical calculation
    if chose.upper() == "QUATERS":
        if quarter == '1st':
            if 0 < chosen <= 12:
                print(f'Your balance is {client + quarters_1st*2}$')
                client += quarters_1st*2
            else:
                client -= quarters_1st
        if quarter == '2nd':
            if 12 < chosen <= 24:
                print(f'Your balance is {client + quarters_2nd*2}$')
                client += quarters_2nd
            else:
                client -= quarters_2nd
        if quarter == '3rd':
            if 24 < chosen <= 36:
                print(f'Your balance is {client + quarters_3rd*2}$')
                client += quarters_3rd
            else:
                client -= quarters_3rd
# lines mathematical calculation
    if chose.upper() == "LINES":
        if lines == "1st":
            if chosen in line_1:
                client += (lines_bet * 2)
            else:
                client -= lines_bet
        if lines == "2nd":
            if chosen in line_2:
                client += (lines_bet * 2)
            else:
                client -= lines_bet
        if lines == "3rd":
            if chosen in line_3:
                client += (lines_bet * 2)
            else:
                client -= lines_bet

    if chose.upper() == "QUATERS":
        print(f"Your balance is {client}$")
    if chose.upper() == "LINES":
        print(f"Your balance is {client}$")
    time.sleep(0.5)
    if client == 0:
        print("You dont have more money.")
        break
    bet = 0
    bet_rounds = 0
    cont = input("Do you want to continoue?\nYes/No\n")
    if cont.upper() == "YES":
        continue
    else:
        print(f"Thanks for the game and congrat for your {client}$")
        break
"""""
Atalakitani a quaters es a line kiirasat, a colornak megfeleloen (client + bet*2 vagy client + bet*3)

******
JAVITVA 2022.08.20.
clientbol folyamatosan vonta ki a bet az osszeget pl ha client = 10k bet = 2k akkor client = 8k ha continoue
tegyuk fel a bet = 4k, akkor eddig ugy csinalta, hogy a korabbi betet is hozza adta, tehat 2k+4K es igy a client = 2k maradt
*****

bet_color_red es bet_color_black bevezetese, hogy megkevesebb eselye legyen osszeakadni, szin szamolasanak atalakitasa,
az uj valtozoknak megefleloen 

"""