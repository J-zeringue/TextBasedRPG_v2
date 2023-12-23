import os
import random
import time
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

# coords of player on map used for movement
x = 7
y = 9


# draws line to seprate text in game play loop
def draw_line():
    print('------------------------')

# function that clears console
def clear():
    os.system("clear")

# battle loop
def battle(enemy):
    global boss, fight, play, run

    draw_line()
    slow_print(f"Enemy {enemy.name} attacks!")
    draw_line()

    while fight:
        print(f"{enemy.name}'s Level: {enemy.level} HP: {enemy.hp}/{enemy.hp_max}")
        print(f"{player.name}'s HP: {player.hp}/{player.hp_max}")
        print(f"Potions: {player.check_potion_inv_count()}")
        draw_line()
        print('1 - Attack')
        if player.check_potion_inv_count() > 0:
            print('2 - Use potion')
        print('4 - Flee')
        draw_line()
        choice = input("> ")

        if choice == '1':
            player.attack(enemy)
            draw_line()
            if enemy.hp > 0:
                enemy.attack(player)

        if choice == '2':
            if player.check_potion_inv_count() > 0:
                potion.use_potion(player)
                draw_line()
                enemy.attack(player)

        if choice == '3':
            pass

        if choice == '4':
            if random.randint(0, 100) >= 33:
                slow_print(f'{player.name} flees from {enemy.name}')
                fight = False
            else:
                slow_print('Your attempt to flee has failed!')

        # checks player health
        if player.hp <= 0:
            slow_print(f'{player.name} has been defeated by {enemy.name}')
            draw_line()
            fight = False
            play = False
            run = False
            slow_print('GAME OVER!')
            input('> ')
            quit()
        # checks enemy health
        if enemy.hp <= 0:
            slow_print(f'{player.name} has defeated {enemy.name}')
            draw_line()
            player.check_xp(enemy)
            draw_line()
            fight = False
            if random.randint(0, 100) < 25:
                potion.add_item_to_inventoy(player)
                slow_print("You found a Health Potion")
            if boss == True:
                slow_print(f'you have defeated {enemy.name}')
                player.check_xp(enemy)
                if not boss_list:
                    boss = False
                    fight = False
                    play = False
                    run = False
                    slow_print('With the four dragons defeated the region can now know peace')
                    slow_print('CONGRATULATIONS! YOU HAVE BEATEN THE GAME!')
                    input('> ')
                    quit()
                else:
                    slow_print(f"Congratulations you have defeated {enemy.name}")
                    boss = False
                    fight = False
                    input('> ')
                    clear()

def cave_boss_battle():
    global boss, fight
    boss = True
    while boss:
        clear()
        draw_line()
        slow_print('A dangerous dragon lies within, will you fight or flee?')
        print('1. Enter')
        print('2. Turn Back')
        choice = input('> ')

        if choice == '1':
            fight = True
            battle(Boss.spawn_boss())
        if choice == '2':
            boss = False


def shop():
    global buy
    while buy:
        clear()
        draw_line()
        slow_print("Welcome to Krupp's mysterous mysterions!")
        draw_line()
        print(f'Gold: {player.gold}')
        print(f'Potions: {player.check_potion_inv_count()}')
        print(f'Current weapon: {player.equipped_weapon.name}')
        print(f'Current armor: {player.equipped_armor.name}')
        draw_line()
        print(f'1. Buy {potion.name} - {potion.g_value} gold.')
        # needs to be a list of armor
        if armor_upgrades:
            print(f'2. Upgrade armor to {armor_upgrades[-1].name} - {armor_upgrades[-1].g_value} gold.')
        # needs to be a list of weapons
        if weapon_upgrades:
            print(f'3. Upgrade weapon to {weapon_upgrades[-1].name} - {weapon_upgrades[-1].g_value} gold.')
        print('4. Exit Shop')
        draw_line()

        choice = input('> ')
        try:
            if choice == '1':
                if player.gold - 5 >= 5:
                    potion.add_item_to_inventoy(player)
                    player.gold -= 5
                    print('Health Potion purchased for 5 gold')
                else:
                    print('Not enough gold!')
            if choice == '2':
                if player.gold - armor_upgrades[-1].g_value >= armor_upgrades[-1].g_value:
                    player.gold -= armor_upgrades[-1].g_value
                    Armor.upgrade_armor(player)
                else:
                    print('Not enough gold!')
            if choice == '3':
                if player.gold - weapon_upgrades[-1].g_value >= weapon_upgrades[-1].g_value:
                    player.gold -= weapon_upgrades[-1].g_value
                    Weapon.upgrade_weapon(player)
                else:
                    print('Not enough gold!')
            if choice == '4':
                buy = False
        except IndexError:
            print('No more upgrades available!')

while run:
    while menu:
        clear()
        print('1. NEW GAME')
        print('2. RULES')
        print('3. QUIT GAME')
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
            player = Character(name, 1, 25, 3, 50, 0)
            player.equipped_armor = leather_armor
            player.equipped_weapon = iron_sword
            draw_line()
            menu = False
            play = True

        if choice == '2':
            rules = True

        if choice == '3':
            quit()

    while play:
        clear()
        # controls battle encounters
        if not standing:
            if biom[map[y][x]]['e'] == True:
                if random.randint(0, 100) <= 0:
                    fight = True
                    battle(Enemy.spawn_random_enemy())

        # shows current player location
        try:
            print(f"Current Location: {biom[map[y][x]]['tile']}")
        except IndexError:
            print("I have moved too far away, I should turn back")
        draw_line()
        print(player.name)
        print(f"HP: {player.hp}/{player.hp_max} Attack: {player.atk}")
        print(f"Potions: {player.check_potion_inv_count()} | Weapon: {player.equipped_weapon.name} | Armor: {player.equipped_armor.name}")
        print(f"Gold: {player.gold} Level: {player.level} EXP: {player.xp}/{player.xp_to_lvl} Coordinates: {x},{y}")
        draw_line()
        # menu for player 
        print("0. Quit")
        if y > 0:
            print("1. North")
        if x < x_len:
            print("2. East")
        if y < y_len:
            print("3. South")
        if x > 0:
            print("4. West")
        if player.check_potion_inv_count() > 0:
            print('5. Use potion')
        if map[y][x] == 'town' or map[y][x] == 'cave' or map[y][x] == 'crypt':
            print(f'7. Enter {map[y][x]}')

        dest = str(input("> "))
        if dest == '0':
            play = False
            menu = True

        if dest == '1':
            if y - 1 >= 0:
                y -= 1
                standing = False
            else: 
                slow_print("You cannot move in that direction")
        if dest == '2':
            if x+1 <= x_len:
                x += 1
                standing = False
            else: 
                slow_print("You cannot move in that direction")
        if dest == '3':
            if y+1 <= y_len:
                y += 1
                standing = False
            else: 
                slow_print("Yoou cannot move in that direction")
        if dest == '4':
            if x - 1 >= 0:
                x -= 1
                standing = False
            else: 
                slow_print("Yoou cannot move in that direction")
        if dest == '5':
            if player.check_potion_inv_count() > 0:
                potion.use_potion(player)
            else:
                print('No potions!')
            input('> ')
            standing = True
        if dest == '7':
            if map[y][x] == 'town':
                buy = True
                shop()
            if map[y][x] == 'cave' or map[y][x] == 'crypt':
                cave_boss_battle()
            else:
                standing = True