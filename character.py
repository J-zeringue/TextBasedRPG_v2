import random

class Character():
    def __init__(self, name, level, xp, hp, mana, atk):
        self.name = name
        self.level = level
        self.xp = xp
        self.xp_to_lvl = 100
        self.hp = hp
        self.hp_max = self.hp
        self.mana = mana
        self.mana_max = self.mana
        self.atk = atk
    
    # checks xp after every battle and levels up player if conditions are met
    def check_xp(self, enemy):
        print(f'{self.name} gains {enemy.xp}')
        self.xp += enemy.xp
        if self.xp >= self.xp_to_lvl:
            self.level += 1
            print(f'{self.name} has reached level {self.level}')
            self.hp_max += 5
            self.mana_max += 2
            self.atk += 1
            print(f'Your health, mana and attack increase to {self.hp_max}, {self.mana_max} and {self.atk}')
            self.xp = self.xp - self.xp_to_lvl
            self.xp_to_lvl = self.xp_to_lvl + (self.level*15)

class Enemy(Character):
    def __init__(self, name, level, xp, hp, mana, atk):
        super().__init__(level, name, xp, hp, mana, atk)


class Boss(Character):
    def __init__(self, name, level, xp, hp, mana, atk):
        super().__init__(level, name, xp, hp, mana, atk)