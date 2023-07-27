import constant as c
class Character:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    
    def buff_atk(self, buff):
        self.attack = self.attack + buff
    
    def buff_hp(self, buff):
        self.health = self.health + buff
    
    def show_stats(self, arg):
        if arg == 1:
            return 1#"Útok: " + str(self.attack) + " HP: " + str(self.health))
        elif arg == 2:
            return self.health
        elif arg == 3:
            return self.attack
        else:
            print("Invalid argument in show_stats()")
    
#class Hero inherits Character 
class Hero(Character):
    type = c.PLAYER
    
#class Monster inherits Monster 
class Monster(Character):
    type = c.MONSTER      
        
    def scream(self):
        print("WAAAAAA")  

class Coms:
    def start_game(self):
        self.i_name = input("Zvol si své jméno: ")
        #self.i_difficulty = input("Vyber obtížnost 1-5: ")
        
    def game_over(self):
        print("Dostali tě, zkus to znovu")
        
    def monster_dead(self, monster_name):
        print(monster_name + " byl poražen, pokračuješ dál")
        
    def round(self, num):
        print("Kolo číslo: " + str(num))
        
        
def check_if_dead(character ):
    notification = Coms()
    
    if character.health <= 0:
        if character.type == c.MONSTER:
            notification.monster_dead(character.name)
        elif character.type == c.PLAYER:
            notification.game_over()
        else:
            print("Bad value")
        #print("game_over")
        return 1
    return 0



def fight(monster, player, i):
    notification = Coms()
    notification.round(i)
    
    print(monster.name + " má " + str(monster.show_stats(2)) + " HP")
    print(player.name + " má " + str(player.show_stats(2)) + " HP")
    
    monster.health = monster.health - player.attack
    player.health = player.health - monster.attack
    
    if not check_if_dead(monster):
        #print("monster live")
        if not check_if_dead(player):
            #print("player live")
            fight(monster, player, i + 1)
            
def encounter(monster, player):
    print("Narazil jsi na " + monster.name + "! Útok: " + str(monster.attack) + " HP: " + str(monster.health))
    fight(monster, player, 1)

chat = Coms()
chat.start_game()
player1 = Hero(chat.i_name, 5, 1)
monster1 = Monster("Vlk", 6, 1)
encounter(monster1, player1)




