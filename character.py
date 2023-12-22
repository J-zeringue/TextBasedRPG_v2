import random
import time
from world import*

class Character():
    def __init__(self, name, level, hp, atk, gold, xp):
        self.name = name
        self.level = level
        self.xp = xp
        self.xp_to_lvl = 100
        self.hp = hp
        self.hp_max = self.hp
        self.atk = atk
        self.gold = gold
        # sets up player and enemy inventory (not used for enemies at the moment)
        self.inventory = [
            [], # 0 potions are stored
            []] # 1 special items stored
        self.equipped_armor = None
        self.equipped_weapon = None

    def check_potion_inv_count(self):
        if not self.inventory[0]:
            return 0
        return len(self.inventory[0])
    
    # checks xp after every battle and levels up player if conditions are met
    def check_xp(self, enemy):
        slow_print(f'{self.name} gains {enemy.xp} experience and {enemy.gold} gold.')
        self.xp += enemy.xp
        self.gold += enemy.gold
        if self.xp >= self.xp_to_lvl:
            self.level += 1
            slow_print(f'{self.name} has reached level {self.level}')
            self.hp_max += 5
            self.atk += 1
            slow_print(f'Your health and attack damage increase to {self.hp_max} and {self.atk}')
            self.xp = self.xp - self.xp_to_lvl
            self.xp_to_lvl = self.xp_to_lvl + (self.level*15)
    
    # function to attack a target
    def attack(self, target):
        damage = 0
        if target.equipped_armor == None:
            if self.equipped_weapon == None:
                damage = self.atk
            if self.equipped_weapon != None:
                damage = self.atk + self.equipped_weapon.atk_rating
            target.hp -= damage
        if target.equipped_armor != None:
            if self.equipped_weapon == None:
                damage = self.atk - target.equipped_armor.armor_rating
            if self.equipped_weapon != None:
                damage = (self.atk + self.equipped_weapon.atk_rating) - target.equipped_armor.armor_rating
            if damage <= target.equipped_armor.armor_rating:
                damage = 0
                target.hp -= damage
            else:
                target.hp -= damage
        if target.equipped_armor == None:
            slow_print(f'{self.name} dealt {damage} damage to {target.name}! {0} resisted by armor!')
        else:
            slow_print(f'{self.name} dealt {damage} damage to {target.name}! {target.equipped_armor.armor_rating} resisted by armor!')


class Enemy(Character):
    def __init__(self, name, level, hp, atk, gold, xp):
        super().__init__(name, level, hp, atk, gold, xp)

    # helper function to increase the level and stats of randomly spawned enemies to the player level:
    def level_up_enemy(self):
        i = 1
        while i <= self.level:
            self.hp += 5
            self.atk += 1
            self.hp_max = self.hp
            self.gold += 2
            self.xp += 2
            i += 1
    
    # generates a random enemy object
    def spawn_random_enemy():
        enemy_type_i = random.randrange(0, len(enemy_list)-1)
        enemy_strength_i = random.randrange(0, len(enemy_list[enemy_type_i])-1)
        if enemy_type_i == 0:
            if enemy_strength_i == 0:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 1, 10, 2, 2, 2)
                enemy.level_up_enemy
            if enemy_strength_i == 1:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 4, 15, 3, 4, 4)
                enemy.level_up_enemy
            if enemy_strength_i == 2:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 8, 20, 5, 8, 8)
                enemy.level_up_enemy
            if enemy_strength_i == 3:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 12, 25, 8, 12, 12)
                enemy.level_up_enemy
            if enemy_strength_i == 4:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 16, 30, 12, 20, 20)
                enemy.level_up_enemy
        if enemy_type_i == 1:
            if enemy_strength_i == 0:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 1, 10, 2, 2, 2)
                enemy.level_up_enemy
            if enemy_strength_i == 1:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 4, 15, 3, 4, 4)
                enemy.level_up_enemy
            if enemy_strength_i == 2:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 8, 20, 5, 8, 8)
                enemy.level_up_enemy
            if enemy_strength_i == 3:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 12, 25, 8, 12, 12)
                enemy.level_up_enemy
            if enemy_strength_i == 4:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 16, 30, 12, 20, 20)
                enemy.level_up_enemy
        if enemy_type_i == 2:
            if enemy_strength_i == 0:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 1, 10, 2, 2, 2)
                enemy.level_up_enemy
            if enemy_strength_i == 1:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 4, 15, 3, 4, 4)
                enemy.level_up_enemy
            if enemy_strength_i == 2:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 8, 20, 5, 8, 8)
                enemy.level_up_enemy
            if enemy_strength_i == 3:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 12, 25, 8, 12, 12)
                enemy.level_up_enemy
            if enemy_strength_i == 4:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 16, 30, 12, 20, 20)
                enemy.level_up_enemy
        if enemy_type_i == 3:
            if enemy_strength_i == 0:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 1, 10, 2, 2, 2)
                enemy.level_up_enemy
            if enemy_strength_i == 1:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 4, 15, 3, 4, 4)
                enemy.level_up_enemy
            if enemy_strength_i == 2:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 8, 20, 5, 8, 8)
                enemy.level_up_enemy
            if enemy_strength_i == 3:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 12, 25, 8, 12, 12)
                enemy.level_up_enemy
            if enemy_strength_i == 4:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 16, 30, 12, 20, 20)
                enemy.level_up_enemy
        if enemy_type_i == 4:
            if enemy_strength_i == 0:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 1, 10, 2, 2, 2)
                enemy.level_up_enemy
            if enemy_strength_i == 1:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 4, 15, 3, 4, 4)
                enemy.level_up_enemy
            if enemy_strength_i == 2:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 8, 20, 5, 8, 8)
                enemy.level_up_enemy
            if enemy_strength_i == 3:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 12, 25, 8, 12, 12)
                enemy.level_up_enemy
            if enemy_strength_i == 4:
                enemy = Enemy(enemy_list[enemy_type_i][enemy_strength_i], 16, 30, 12, 20, 20)
                enemy.level_up_enemy
        return enemy


class Boss(Character):
    def __init__(self, name, level, hp, atk, gold, xp):
        super().__init__(name, level, hp, atk, gold, xp)
    
    # helper function to increase the stats of bosses when they spawn
    def level_up_enemy(self, player):
        i = 1
        while i <= self.level:
            self.hp += 5
            self.atk += 1
            self.hp_max = self.hp
            self.gold += 2
            self.xp += 2
            i += 1

    # spawns 1 of the 4 bosses at random
    def spawn_boss():
        boss_choice = random.randrange(0, len(boss_list)-1)
        enemy = boss_list.pop(boss_choice)
        return enemy


class Item():
    def __init__(self, name, g_value, category):
        self.name = name
        self.g_value = g_value
        self.category = category
        
    def add_item_to_inventoy(self, character):
        if self.category == 'potion':
            character.inventory[0].append(self)
        if self.category == 'special':
            character.inventory[1].append(self)
    
    def remove_item_from_inventory(self, character):
        if self.category == 'potion':
            character.inventory[0].remove(self)
        if self.category == 'special':
            character.inventory[1].remove(self)

class Potion(Item):
    def __init__(self, name, g_value, category):
        super().__init__(name, g_value, category)
    
        
    def use_potion(self, character):
        amount = character.hp_max*0.75
        if character.hp + amount <= character.hp_max:
            character.hp += amount
            slow_print(f'{character.name} uses a potion and heals for {amount}!')
        else:
            character.hp = character.hp_max
            slow_print(f'{character.name} uses a potion and heals to full health!')
        self.remove_item_from_inventory(character)

class Weapon(Item):
    def __init__(self, name, g_value, category, atk_rating):
        super().__init__(name, g_value, category)
        self.atk_rating = atk_rating
        
    
    #upgrades weapon by replacing it with a created weapon, to be used in the shop
    def upgrade_weapon(character):
        new_weapon = weapon_upgrades.pop()
        character.equipped_weapon = new_weapon
        slow_print(f'Weapon upgraded to {character.equipped_weapon.name}!')

class Armor(Item):
    def __init__(self, name, g_value, category, armor_rating):
        super().__init__(name, g_value, category)
        self.armor_rating = armor_rating

    #upgrades armor by replacing it with a created weapon, to be used in the shop
    def upgrade_armor(character):
        new_armor = armor_upgrades.pop()
        character.equipped_armor = new_armor
        slow_print(f'Armor upgraded to {character.equipped_armor.name}!')


def slow_print(words):
    for word in words:
        time.sleep(0.03)
        print(word, end='', flush=True)
    print('')


# creates potion object
potion = Potion('Health Potion', 10, 'potion')

# creates new weapons
iron_sword = Weapon('Iron Sword', 5, 'weapon', 1)
steel_sword = Weapon('Steel Sword', 100, 'weapon', 3)
obsidian_sword = Weapon('Obsidian Sword', 300, 'weapon', 6)
mithril_sword = Weapon('Mithril Sword', 400, 'weapon', 9)
meteor_sword = Weapon('Meteorite Sword', 600, 'weapon', 15)

# weapon queue for shop upgrades
weapon_upgrades = [meteor_sword, mithril_sword, obsidian_sword, steel_sword]

# creates new armors
leather_armor = Armor('Leather Armor', 5, 'armor', 1)
chain_armor = Armor('Chainmail', 100, 'armor', 3)
plate_armor = Armor('Steel Plate', 200, 'armor', 5)
mithril_armor = Armor('Mithril Half-Plate', 400, 'armor', 7)
meteor_armor = Armor('Meteorite Full-Plate', 600, 'armor', 12)

# armor for dragon bosses
dragon_scale = Armor('Dragon Scales', 1000, 'armor', 15)

# armor queue for shop upgrades
armor_upgrades = [meteor_armor, mithril_armor, plate_armor, chain_armor]

# Boss objects
black_dragon = Boss('Anomandarus Son of Darkness', 75, 100, 20, 1000, 150)
black_dragon.equipped_armor = dragon_scale

red_dragon = Boss('Korlat Daughter of Darkness', 50, 100, 20, 1000, 150)
red_dragon.equipped_armor = dragon_scale

blue_dragon = Boss('Orlock Son of Chaos', 35, 100, 20, 1000, 150)

white_dragon = Boss('Silanus Daughter of Chaos', 25, 100, 20, 1000, 150)

# Boss list for random spawning
boss_list = [black_dragon, red_dragon, blue_dragon, white_dragon]