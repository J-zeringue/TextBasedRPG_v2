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
            [], # 1 weapons are stored
            [], # 2 armor will be stored
            []] # 3 special is stored
        self.equipped_armor = leather_armor
        self.equipped_weapon = iron_sword

    def check_potion_inv_count(self):
        if not self.inventory[0]:
            return 0
        return len(self.inventory[0])
    
    # checks xp after every battle and levels up player if conditions are met
    def check_xp(self, enemy):
        if self.level < 20:
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
        else:
            return
    
    # function to attack a target
    def attack(self, target):
        target.hp -= self.atk
        slow_print(f'{self.name} dealt {self.atk} damage to {target.name}')


class Enemy(Character):
    def __init__(self, name, level, hp, atk, gold, xp):
        super().__init__(name, level, hp, atk, gold, xp)

    # helper function to increase the level and stats of randomly spawned enemies to the player level:
    def level_up_enemy(self, player):
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
        super().__init__(name, level, hp, atk, gold=0, xp=0)



class Item():
    def __init__(self, name, g_value, category):
        self.name = name
        self.g_value = g_value
        self.category = category
        
    def add_item_to_inventoy(self, character):
        if self.category == 'potion':
            character.inventory[0].append(self)
        if self.category == 'weapon':
            character.inventory[1].append(self)
        if self.category == 'armor':
            character.inventory[2].append(self)
        if self.category == 'special':
            character.inventory[3].append(self)
    
    def remove_item_from_inventory(self, character):
        if self.category == 'potion':
            character.inventory[0].remove(self)
        if self.category == 'weapon':
            character.inventory[1].remove(self)
        if self.category == 'armor':
            character.inventory[2].remove(self)
        if self.category == 'special':
            character.inventory[3].remove(self)

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
    def __init__(self, name, g_value, category, atk_rating, armor_ignore):
        super().__init__(name, g_value, category)
        self.atk_rating = atk_rating
        self.armor_ignore = armor_ignore
    
    def equip_weapon(self, character):
        character.equip_weapon == None
        character.equip_weapon = self
        print(f'{character.equip_weapon.name} has been equipped')

class Armor(Item):
    def __init__(self, name, g_value, category, armor_rating):
        super().__init__(name, g_value, category)
        self.armor_rating = armor_rating
    
    def equip_armor(self, character):
        character.equipped_armor == None
        character.equipped_armor = self
        slow_print(f'{character.equipped_armor.name} has been equipped')


def slow_print(words):
    for word in words:
        time.sleep(0.05)
        print(word, end='', flush=True)
    print('')


# creates potion object

potion = Potion('Health Potion', 5, 'potion')

iron_sword = Weapon('Iron Sword', 5, 'weapon', 1, 0)




leather_armor = Armor('Leather Armor', 5, 'armor', 1)