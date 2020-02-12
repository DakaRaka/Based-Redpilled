from random import randint as rand


class Monster():
    def __init__(self, name='UNKOWN'):
        self.name = name
        self.damage = rand(0, 10)
        self.health = (1, 3)
        self.battlecry = 'YEAAAAARGH!'

    def __str__(self):
        return f'A monster called {self.name}'

class WarCat(Monster):
    def __init__(self, name="WarCat"):
        super().__init__(name)
        self.damage = rand(3, 12)
        self.health = (12)
        self.battlecry = 'Meow'

class Warlock(Monster):
    def __init__(self, name="Warlock"):
        super().__init__(name)
        self.name = name
        self.health = (12)
        self.battlecry = 'Burppppppp'

class Masterwarlock(Warlock):
    def __init__(self, name='Warlock'):
        super().__init__(name)
        self.name = name
        self.health = (30)
        self.damage = rand(5, 10)
        self.battlecry = 'BURPPPPPPPPPPPPPPPPPPPPPPPPPPPPPpPPPP!'