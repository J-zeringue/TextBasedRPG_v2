import random
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
    
    # checks xp after every battle and levels up player if conditions are met
    def check_xp(self, enemy):
        if self.level < 20:
            print(f'{self.name} gains {enemy.xp} experience and {enemy.gold} gold.')
            self.xp += enemy.xp
            self.gold += enemy.gold
            if self.xp >= self.xp_to_lvl:
                self.level += 1
                print(f'{self.name} has reached level {self.level}')
                self.hp_max += 5
                self.atk += 1
                print(f'Your health and attack damage increase to {self.hp_max} and {self.atk}')
                self.xp = self.xp - self.xp_to_lvl
                self.xp_to_lvl = self.xp_to_lvl + (self.level*15)
        else:
            return

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
        enemy_type_i = random.randrange(0, len(enemy_list))
        enemy_strength_i = random.randrange(0, len(enemy_list[enemy_type_i]))
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