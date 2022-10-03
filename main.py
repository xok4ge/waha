import random


class PLayer:
    def __init__(self, name, order, specialization):
        self.name = name
        self.order = order
        self.spec = specialization
        self.hp = 100
        self.dmg_hand = 12
        self.mana = 100
        self.armour = 0
        self.inventory = []

    def __str__(self):
        return f'Ваше имя {self.name}. Вы {self.spec} ордена {self.order}'


class NekronInfantry:
    def __init__(self):
        self.hp = 75
        self.dmg = 16
        self.armour = 2


class Treasure:
    def __init__(self):
        self.rarity = 'legendary'
        self.diff = 'hell'
        self.gold = random.randint(900, 1250)
        
