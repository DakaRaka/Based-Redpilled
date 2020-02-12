import Monsters
import Player
from random import randint as rand

running = True

monsters = [Monsters.WarCat, Monsters.Warlock, Monsters.Masterwarlock]

intro = """Welcome to the grand adventure game

We hope you like being attacked by monsters.

Choose your class:

1) Warrior
2) Paladin
"""

print(intro)
playerinput = input("What class do you want?: ").capitalize()
playername = input("What is your name?: ").capitalize()


if playerinput == "Warrior":
    player = Player.Warrior(playername)
elif playerinput == "Paladin":
    player = Player.Paladin(playername)

for constructor in monsters:
    monster = constructor()
    monsterchoice = input("""What monster would you like to fight
    1) Warcat
    2) Warlock
    3) Masterwarlock: """).capitalize()     
    if monsterchoice == "Warcat":
        Playerstarthp = Player.Player("Brugj")
        player_hp = Playerstarthp.health
        Warcatstarthp = Monsters.WarCat("bruh")
        Warcat_HP = Warcatstarthp.health
        alive = True
        while alive: 
            Warcatstart = Monsters.WarCat("bruh")
            Playerstart = Player.Player("bruh")
            Warcat_DMG = Warcatstart.damage
            Player_DMG = Playerstart.damage
            player_hp = player_hp - Warcat_DMG
            Warcat_HP = Warcat_HP - Player_DMG
            print (f"You attack the Warcat and you deal {Player_DMG} the warcat has {Warcat_HP} left")
            print (f"The Warcat attacks you and deals {Warcat_DMG} you have {player_hp} left")
            if Warcat_HP < 0:
                print(("You got em"))
                alive = False
            if player_hp < 0 :
                exit("YOU DIED PISS OFF YOU DISGUSTING CASUAL ADVENTURER")
            

    elif monsterchoice == "Warlock":
        #Sorry for the lazyness it is quite late 
        Playerstarthp = Player.Player("Brugj")
        player_hp = Playerstarthp.health
        Warlockstarthp = Monsters.Warlock("bruh")
        Warlock_HP = Warlockstarthp.health
        alive = True
        while alive: 
            Warlockstart = Monsters.Warlock("bruh")
            Playerstart = Player.Player("bruh")
            Warlock_DMG = Warlockstart.damage
            Player_DMG = Playerstart.damage
            player_hp = player_hp - Warlock_DMG
            Warlock_HP = Warlock_HP - Player_DMG
            print (f"You attack the Warlock and you deal {Player_DMG} the warcat has {Warlock_HP} left")
            print (f"The Warlock attacks you and deals {Warlock_DMG} you have {player_hp} left")
            if Warlock_HP < 0:
                print("You got em")
                alive = False
            if player_hp < 0 :
                exit("YOU DIED PISS OFF YOU DISGUSTING CASUAL ADVENTURER")

    elif monsterchoice == "Masterwarlock":
        Playerstarthp = Player.Player("Brugj")
        player_hp = Playerstarthp.health
        Masterwarlockstarthp = Monsters.Masterwarlock("bruh")
        Masterwarlock_HP = Masterwarlockstarthp.health
        alive = True
        while alive: 
            Masterwarlockstart = Monsters.Masterwarlock("bruh")
            Playerstart = Player.Player("bruh")
            Masterwarlock_DMG = Masterwarlockstart.damage
            Player_DMG = Playerstart.damage
            player_hp = player_hp - Masterwarlock_DMG
            Masterwarlock_HP = Masterwarlock_HP - Player_DMG
            print (f"You attack the Masterwarlock and you deal {Player_DMG} the Masterwarlock has {Masterwarlock_HP} left")
            print (f"The Masterwarlock attacks you and deals {Masterwarlock_DMG} you have {player_hp} left")
            if Masterwarlock_HP < 0:
                print("You got em")
                alive = False
            if player_hp < 0 :
                exit("YOU DIED PISS OFF YOU DISGUSTING CASUAL ADVENTURER")
        
