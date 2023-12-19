import os

run = True
menu = True
play = False
rules = False
key = False

hp = 50
atk = 3
potions = 1
elixirs = 0
gold = 0
x = 0
y = 0

def clear():
    os.system("cls")

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

        if rules:
            print("something")
            rules = False
            choice = ''
            input(': ')

        choice = input(': ')

        if choice == '1':
            clear()
            name = input('What is your name? ')
            menu = False
            play = True
        if choice == '2':
            try:
                f = open('load.txt', 'r')
                save_file = f.readlines
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
            except OSError:
                print("No save file exists")
                input(': ')
        if choice == '3':
            rules = True
        if choice == '4':
            quit()
    while play:
        save() # auto saves game
        print(name)

        dest = input(";")
        if dest == '0':
            play = False
            menu = True