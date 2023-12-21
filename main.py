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

potions = 1
elixirs = 0
gold = 0
# coords of player on map
x = 0
y = 0


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

# saves player stats by writing to a text file
def save():
    player_stats = [
        player.name,
        str(player.level),
        str(player.xp), 
        str(player.hp),
        str(player.atk),
        str(potions),
        str(elixirs),
        str(player.gold),
        str(x),
        str(y),
        str(key)
    ]

    f = open('load.txt,', 'w')

    for item in player_stats:
        f.write(item + '\n')
    f.close()

def use_potion(amount):
    if player.hp + amount <= player.hp_max:
        player.hp += amount
    else:
        player.hp = player.hp_max
    print(f'{player.name} uses a potion and heals for {amount}')

def battle(enemy):
    global potions, elixirs, boss, fight
    print('found fight')
    
    while fight:
        clear()
        draw_line()
        print(f"Enemy {enemy.name} attacks!")
        draw_line()
        print(f"{enemy.name}'s HP: {enemy.hp}/{enemy.hp_max}")
        print(f"{player.name}'s HP: {player.hp}/{player.hp_max}")
        print(f"Potions: {potions}")
        print(f"Elixirs: {elixirs}")
        draw_line()
        print('1 - Attack')
        if potions > 0:
            print('2 - Use potion')
        if elixirs > 0:
            print('3 - Use elixir')
        draw_line()
        choice = input(": ")

        if choice == '1':
            enemy.hp -= player.atk
            print(f'{player.name} dealt {player.atk} damage to {enemy.name}')
            if enemy.hp > 0:
                player.hp -= enemy.atk
                print(f'{enemy.name} attacks {player.name} for {enemy.atk} damage')

        if choice == '2':
            if potions > 0:
                potions -= 1
                use_potion(30)
                player.hp -= enemy.atk
                print(f'{enemy.name} attacks {player.name} for {enemy.atk} damage')

        if choice == '3':
            if elixirs > 0:
                elixirs -= 1
                use_potion(30)
                player.hp -= enemy.atk
                print(f'{enemy.name} attacks {player.name} for {enemy.atk} damage')

        # checks player health
        if player.hp <= 0:
            print(f'{player.name} has been defeated by {enemy.name}')
            draw_line()
            fight = False
            play = False
            run = False
            print('GAME OVER!')
            input(': ')
            quit()
        # checks enemy health
        if enemy.hp <= 0:
            print(f'{player.name} has defeated {enemy.name}')
            draw_line()
            player.check_xp(enemy)
            draw_line()
            fight = False
            if random.randint(0, 100) < 30:
                potions += 1
                print("You found a potion")
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
    global buy, potions, elixirs
    while buy:
        clear()
        draw_line()
        print("Welcome to Krupp's mysterous mysterions!")
        draw_line()
        print(f'Gold: {player.gold}')
        print(f'Potions: {potions}')
        print(f'Elixirs: {elixirs}')
        print(f'Attack damage: {player.atk}')
        draw_line()
        print('1. Buy potion (heal for 30 HP) - 5 gold')
        print('2. Buy elixir (heal for 50 HP) - 10 gold')
        print('3. Upgrade weapon (+ 2 to attack) - 15 gold')
        print('4. Exit Shop')
        draw_line()

        choice = input('> ')

        if choice == '1':
            if player.gold - 5 >= 5:
                potions += 1
                player.gold -= 5
                print('Potion purchased for 5 gold')
            else:
                print('Not enough gold!')
        if choice == '2':
            if player.gold - 10 >= 10:
                elixirs += 1
                player.gold -= 10
                print('Elixir purchased for 5 gold')
            else:
                print('Not enough gold!')
        if choice == '3':
            if player.gold - 15 >= 15:
                player.atk += 2
                player.gold -= 15
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
            player = Character(name, 1, 10, 2, 0, 0 )
            draw_line()
            menu = False
            play = True

        if choice == '2':
            # handles error if file does not exist
            try:
                f = open('load.txt', 'r')
                save_file = f.readlines
                # checks if file has all the proper data
                if len(save_file) == 11:
                    name = save_file[0]
                    lvl = int(save_file[1])
                    xp = int(save_file[2])
                    hp = int(save_file[3])
                    atk = int(save_file[4])
                    potions = int(save_file[5])
                    elixirs = int(save_file[6])
                    gold = int(save_file[7])
                    x = int(save_file[8])
                    y = int(save_file[9])
                    key = bool(save_file[10])
                    player = Character(name, lvl, hp, atk, gold, xp)
                    clear()
                    print(f'welcome back {player.name} to your adventure!')
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
                if random.randint(0, 100) <= 40:
                    fight = True
                    battle(Enemy.spawn_random_enemy())
                    
        # shows current player location
        try:
            print(f"Current Location: {biom[map[x][y]]['tile']}")
        except IndexError:
            print("I have moved too far away, I should turn back")
        draw_line()
        print(player.name)
        print(f"HP: {player.hp}/{player.hp_max}")
        print(f"Attack: {player.atk}")
        print(f"Potions: {potions}")
        print(f"Elixirs: {elixirs}")
        print(f"Gold: {player.gold}")
        print(f"Coordinates: {x},{y}")
        print(standing)
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
        if map[y][x] == 'shop' or map[y][x] == 'cave' or map[y][x] == 'crypt':
            print(f'7. Enter {map[y][x]}')

        dest = str(input("> "))
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