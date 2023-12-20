import os

run = True
menu = True
play = False
rules = False
key = False

hp = 50
hp_max = hp
atk = 3
potions = 1
elixirs = 0
gold = 0
x = 0
y = 0

# creates map
    # x     0        1          2         3        4        5          6         7      y
map = [['mountain', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 0  
       ['mountain', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains'], # 1
       ['mountain', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains'], # 2
       ['mountain', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains'], # 3
       ['mountain', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains'], # 4
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains'], # 5
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains'], # 6
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains'],]# 7

x_len = len(map) - 1
y_len = len(map[0]) - 1



biom = {
    'plains':{
        'tile': 'PLAINS',
        'e': True},
    'forest':{
        'tile': 'WOODS',
        'e': True},
    'fields':{
        'tile': 'FIELDS',
        'e': False},
    'bridge':{
        'tile': 'BRIDGE',
        'e': True},
    'town':{
        'tile': 'TOWN HUB',
        'e': False},
    'shop':{
        'tile': 'SHOP',
        'e': False},
    'desert':{
        'tile': 'DESERT',
        'e': True},
    'cave':{
        'tile': 'CAVE',
        'e': True},
    'crypt':{
        'tile': 'crypt',
        'e': True},
    'mountain':{
        'tile': 'MOUNTAINS',
        'e': True},
    'hill':{
        'tile': 'HILL',
        'e': True},
}

current_tile = map[x][y]
print(current_tile)
name_of_tile = biom[current_tile]['tile']
print(name_of_tile)
enemy_tile = biom[current_tile]['e']
print(enemy_tile)

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
        dest = str(input(";"))
        if dest == '0':
            play = False
            menu = True
        if dest == '1':
            y -= 1
        if dest == '2':
            x += 1
        if dest == '3':
            y += 1
        if dest == '4':
            x -= 1
        