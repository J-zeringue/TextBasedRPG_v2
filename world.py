import os
import random
from character import*

# creates map
    # x     0        1          2         3        4        5          6         7          y
map = [['mountain', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 0  
       ['mountain', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 1
       ['mountain', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 2
       ['mountain', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 3
       ['mountain', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 4
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 5
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 6
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 7
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 8
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 9
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 10
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 11
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 12
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 13
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 14
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 15
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 16
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 17
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'], # 18
       ['plains', 'plains', 'plains', 'plains','plains', 'plains', 'plains', 'plains', 'desert', 'plains','desert', 'plains', 'plains', 'plains'],]# 19

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