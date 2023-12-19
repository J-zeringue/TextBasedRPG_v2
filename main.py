import os

run = True
menu = True
play = False
rules = False

hp = 50
atk = 3

def clear():
    os.system("cls")

def save():
    player_stats = [
        name, 
        str(hp),
        str(atk),
    ]

    f = open('load.txt,', 'w')

    for item in player_stats:
        f.write(item + '\n')
    f.close()

while run:
    while menu:
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
            name = input('What is your name? ')
            menu = False
            play = True
        if choice == '2':
            f = open('load.txt', 'r')
            save_file = f.readlines
            name = save_file[0]
            hp = save_file[1]
            atk = save_file[2]
            print(f'welcome back {name} to your adventure!')
            input(': ')
            menu = False
            play = True
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