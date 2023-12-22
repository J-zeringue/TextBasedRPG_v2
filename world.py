import os
import random


# creates map
    # x     0        1          2         3        4        5          6         7          8         9         10       11         12        13      y
map = [['mountain', 'desert', 'desert', 'plains','desert', 'plains', 'plains', 'plains', 'desert', 'hill','desert', 'plains', 'plains', 'plains'], # 0  
       ['mountain', 'desert', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'hill','desert', 'plains', 'plains', 'plains'], # 1
       ['mountain', 'desert', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'hill','desert', 'plains', 'plains', 'plains'], # 2
       ['mountain', 'desert', 'desert', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'hill','desert', 'plains', 'plains', 'plains'], # 3
       ['desert', 'desert', 'cave', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'desert','desert', 'plains', 'crypt', 'mountain'], # 4
       ['desert', 'desert', 'desert', 'plains','plains', 'plains', 'fields', 'plains', 'desert', 'desert','desert', 'plains', 'mountain', 'plains'], # 5
       ['desert', 'desert', 'desert', 'plains','plains', 'fields', 'bridge', 'fields', 'desert', 'oasis','desert', 'plains', 'mountain', 'plains'], # 6
       ['hill', 'hill', 'plains', 'plains','plains', 'fields', 'town', 'town', 'desert', 'desert','desert', 'plains', 'mountain', 'plains'], # 7
       ['hill', 'hill', 'plains', 'bridge','fields', 'fields', 'town', 'town', 'fields', 'bridge','desert', 'plains', 'mountain', 'plains'], # 8
       ['hill', 'hill', 'plains', 'plains','plains', 'fields', 'town', 'town', 'desert', 'hill','desert', 'plains', 'mountain', 'plains'], # 9
       ['hill', 'hill', 'plains', 'plains','plains', 'plains', 'bridge', 'plains', 'desert', 'hill','desert', 'plains', 'plains', 'mountain'], # 10
       ['forest', 'forest', 'forest', 'hill','mountain', 'hill', 'fields', 'plains', 'desert', 'hill','desert', 'plains', 'plains', 'plains'], # 11
       ['plains', 'plains', 'forest', 'hill','mountain', 'mountain', 'hill', 'plains', 'desert', 'hill','desert', 'plains', 'plains', 'plains'], # 12
       ['forest', 'forest', 'forest', 'hill','mountain', 'mountain', 'mountain', 'hill', 'desert', 'hill','desert', 'plains', 'plains', 'plains'], # 13
       ['forest', 'forest', 'forest', 'hill','mountain', 'mountain', 'hill', 'plains', 'desert', 'hill','desert', 'plains', 'plains', 'plains'], # 14
       ['forest', 'forest', 'forest', 'hill','mountain', 'plains', 'hill', 'plains', 'desert', 'hill','desert', 'plains', 'plains', 'plains'], # 15
       ['forest', 'forest', 'forest', 'hill','plains', 'plains', 'plains', 'plains', 'desert', 'oasis','desert', 'plains', 'crypt', 'plains'], # 16
       ['forest', 'cave', 'forest', 'hill','hill', 'hill', 'plains', 'plains', 'desert', 'hill','desert', 'plains', 'plains', 'plains'], # 17
       ['mountain', 'mountain', 'mountain', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'],]# 18

y_len = len(map) - 1
x_len = len(map[0]) - 1
       
       

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
    'oasis':{
        'tile': 'OASIS',
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

enemy_list = [
    ['Goblin', 'Goblin Fighter', 'Goblin Rogue', 'Goblin Tinker', 'Goblin Leader'],
    ['Orc Peon', 'Orc Warrior', 'Orc Scout' 'Orc Berserker', 'Orc Cheiftan'],
    ['Green Slime', 'Red Slime', 'Blue Slime', 'Yellow Slime', 'Purple Slime'],
    ['Skeleton', 'Skeleton Archer', 'Skeleton Fighter', 'Skeleton Wizard', 'Skeleton Lord'],
    ['Zombie', 'Mummy', 'Zombie Lord', 'Mummy Lord', 'Mummy Warrior Lord'],
    ['Kobold', 'Kobold Warrior', 'Kobold Scout', 'Kobold Mage', 'Kobold Cheiftan']]