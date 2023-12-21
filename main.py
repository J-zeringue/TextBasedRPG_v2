import os
import random
from character import*
from world import*

# booleans to control game play loop
run = True
menu = True
play = False
rules = False
key = False
fight = False
standing = True
buy = False
speak = False
boss = False

h_p = 50
hp_max = h_p
attk = 3
potions = 1
elixirs = 0
gold = 0
x = 0
y = 0

enemy_list = ['Goblin', 'Orc', 'Slime']

mobs = {
    'Goblin':{
        'hp': 15,
        'atk': 3,
        'gold': 5
    },
    'Orc':{
        'hp': 35,
        'atk': 5,
        'gold': 10
    },    
    'Slime':{
        'hp': 30,
        'atk': 2,
        'gold': 10
    }
}

#current_tile = map[x][y]
#print(current_tile)
#name_of_tile = biom[current_tile]['tile']
#print(name_of_tile)
#enemy_tile = biom[current_tile]['e']
#print(enemy_tile)

# draws line to seprate text in game play loop
def draw_line():
    print('|----------------------|')

# function that clears console
def clear():
    os.system("clear")

def save():
    player_stats = [
        name, 
        str(hp),
        str(atk),
        str(potions),
        str(elixirs),
        str(gold),
        str(x),
        str(y),
        str(key)
    ]

    f = open('load.txt,', 'w')

    for item in player_stats:
        f.write(item + '\n')
    f.close()

def use_potion(amount):
    global h_p, hp_max
    if h_p + amount <= hp_max:
        h_p += amount
    else:
        h_p = hp_max
    print(f'{name} uses a potion and heals for {h_p + amount}')

def battle():
    global h_p, attk, hp_max, gold, potions, elixirs, boss

    if not boss:
        enemy = random.choice(enemy_list)
    else:
        enemy = 'Boss'
    hp = mobs[enemy][hp]
    hpmax = hp
    atk = mobs[enemy][atk]
    g = mobs[enemy][gold]

    while fight:
        clear()
        draw_line()
        print(f"Enemy {enemy} attacks!")
        draw_line()
        print(f"{enemy}'s HP: {hp}/{hpmax}")
        print(f"{name}'s HP: {h_p}/{hp_max}")
        print(f"Potions: {potions}")
        print(f"Elixirs: {elixirs}")
        draw_line()
        print('1 - Attack')
        if potions > 0:
            print('2 - Use potion')
        if elixirs > 0:
            print('2 - Use elixir')
        draw_line()
        choice = input(": ")

        if choice == '1':
            hp -= attk
            print(f'{name} dealt {attk} damage to {enemy}')
            if hp > 0:
                h_p -= atk
                print(f'{enemy} attacks {name} for {atk} damage')

        if choice == '2':
            if potions > 0:
                potions -= 1
                use_potion(30)
                h_p -= atk
                print(f'{enemy} attacks {name} for {atk} damage')

        if choice == '3':
            if elixirs > 0:
                elixirs -= 1
                use_potion(30)
                h_p -= atk
                print(f'{enemy} attacks {name} for {atk} damage')

        # checks player health
        if h_p <= 0:
            print(f'{name} has been defeated by {enemy}')
            draw_line()
            fight = False
            play = False
            run = False
            print('GAME OVER!')
            input(': ')
            quit()
        # checks enemy health
        if hp <= 0:
            print(f'{name} has defeated {enemy}')
            draw_line()
            fight = False
            gold += g
            if random.randint(0, 100) < 30:
                potions += 1
                print("You dound a potion")
            if enemy == 'Boss':
                print("Congratulations you have defeated the Boss")
                boss = False
            input('> ')
            clear()

def cave_boss_battle():
    global boss, key, fight

    while boss:
        clear()
        draw_line()
        # place holder until more bosses are built out
        print('A dangerous boss lies within, will you fight or flee?')
        if key:
            print('1. Use key')
        print('2. Turn Back')
        choice = input('> ')

        if choice == '1':
            if key:
                fight = True
                battle()
        if choice == '2':
            boss = False


def shop():
    global buy, gold, potions, elixirs, attk
    while buy:
        clear()
        draw_line()
        print("Welcome to Krupp's mysterous mysterions!")
        draw_line()
        print(f'Gold: {gold}')
        print(f'Potions: {potions}')
        print(f'Elixirs: {elixirs}')
        print(f'Attack damage: {attk}')
        draw_line()
        print('1. Buy potion (heal for 30 HP) - 5 gold')
        print('2. Buy elixir (heal for 50 HP) - 10 gold')
        print('3. Upgrade weapon (+ 2 to attack) - 15 gold')
        print('4. Exit Shop')
        draw_line()

        choice = input('> ')

        if choice == '1':
            if gold - 5 >= 5:
                potions += 1
                gold -= 5
                print('Potion purchased for 5 gold')
            else:
                print('Not enough gold!')
        if choice == '2':
            if gold - 10 >= 10:
                elixirs += 1
                gold -= 10
                print('Elixir purchased for 5 gold')
            else:
                print('Not enough gold!')
        if choice == '3':
            if gold - 15 >= 15:
                attk += 2
                gold -= 15
                print('Weapon upgrade purchased for 5 gold')
            else:
                print('Not enough gold!')
        if choice == '4':
            buy = False

while run:
    while menu:
        clear()
        print('1. NEW GAME')
        print('2. LOAD GAME')
        print('3. RULES')
        print('4. QUIT GAME')
        draw_line()

        if rules:
            print("something")
            rules = False
            choice = ''
            input(': ')

        choice = input(': ')

        if choice == '1':
            clear()
            name = input('What is your name? ')
            draw_line()
            menu = False
            play = True
        if choice == '2':
            # handles error if file does not exist
            try:
                f = open('load.txt', 'r')
                save_file = f.readlines
                # checks if file has all the proper data
                if len(save_file) == 9:
                    name = save_file[0]
                    hp = int(save_file[1])
                    atk = int(save_file[2])
                    potions = int(save_file[3])
                    elixirs = int(save_file[4])
                    gold = int(save_file[5])
                    x = int(save_file[6])
                    y = int(save_file[7])
                    key = bool(save_file[8])
                    clear()
                    print(f'welcome back {name} to your adventure!')
                    input(': ')
                    menu = False
                    play = True
                else:
                    print('File is corrupt')
                    draw_line()
            except OSError:
                print("No save file exists")
                draw_line()
                input(': ')
        if choice == '3':
            rules = True
        if choice == '4':
            quit()
    while play:
        save() # auto saves game
        clear()
        # controls battle encounters
        if not standing:
            if biom[map[x][y]]['e'] == True:
                if random.randint(0, 100) <= 30:
                    battle()
        # shows current player location
        print(f"Current Location: {biom[map[x][y]]['tile']}")
        draw_line()
        print(name)
        print(f"HP: {hp}/{hp_max}")
        print(f"Attack: {atk}")
        print(f"Potions: {potions}")
        print(f"Elixirs: {elixirs}")
        print(f"Gold: {gold}")
        draw_line()
        # menu for player 
        print("0. Save and quit")
        if y > 0:
            print("1. North")
        if x < x_len:
            print("2. East")
        if y < y_len:
            print("3. South")
        if x > 0:
            print("4. West")
        if potions > 0:
            print('5. Use potion')
        if elixirs > 0:
            print('6. Use elixir')
        if map[y][x] == 'shop' or map[y][x] == 'cave':
            print(f'7. Enter {map[y][x]}')

        dest = str(input(";"))
        if dest == '0':
            play = False
            menu = True
        if dest == '1':
            y -= 1
            standing = False
        if dest == '2':
            x += 1
            standing = False
        if dest == '3':
            y += 1
            standing = False
        if dest == '4':
            x -= 1
            standing = False
        if dest == '5':
            if potions > 0:
                potions -= 1
                use_potion(30)
            else:
                print('No potions!')
            input('> ')
            standing = True
        if dest == '6':
            if elixirs > 0:
                elixirs -= 1
                use_potion(50)
            else:
                print('No elixirs!')
            input('> ')
            standing = True
        if dest == '7':
            if map[y][x] == 'shop':
                buy = True
                shop()
            if map[y][x] == 'cave':
                cave_boss_battle()
        else:
            standing = True