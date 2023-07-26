#class hero
class Hero:
    attack = 1
    health = 1
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
    def buff_atk(self, buff):
        self.attack = self.attack + buff
    def buff_hp(self, buff):
        self.health = self.health + buff
    def show_stats(self):
        print("attack> ")
        print(self.attack)
        print("defense")
        print(self.health)
        

#class monster 
class Monster:        
    def __init__(self, name, health, attack):
        self.monster_name = name
        self.monster_health = health
        self.monster_attack = attack
        self.scream()
        
    def scream(self):
        print("WAAAAAA")  

class Coms:
    def __init__():
        print("Vítám tě u mé hry, prosím zvol si své jméno: \n")
    def game_over():
        print("Dostali tě, zkus to znovu")

x = Hero("X", 3)
x.show_stats()
x.buff_atk(3)
x.show_stats()