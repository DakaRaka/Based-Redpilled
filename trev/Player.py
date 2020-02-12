from random import randint as rand

class Player():
    def __init__(self, name='UNKOWN'):
        self.name = name
        self.profession = False
        self.damage = rand(100, 101)
        self.health = (15)

    def __str__(self):
        return self.profession

class Paladin(Player):
    def __init__(self, name):
        super().__init__(name)
        self.profession = "Paladin"
        self.damage = rand(100, 101)

class Warrior(Player):
    def __init__(self,name):
        super().__init__(name)
        self.profession = 'Warrior'
        self.damage = rand(100, 101)
        




