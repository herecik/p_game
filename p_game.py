import constant as c
#class hero
class Hero:
    type = c.PLAYER
    attack = 1
    health = 10
    
    def __init__(self, name, difficulty):
        self.name = name
        self.difficulty = difficulty
    
    def buff_atk(self, buff):
        self.attack = self.attack + buff
    
    def buff_hp(self, buff):
        self.health = self.health + buff
    
    def show_stats(self):
        print("attack>" + str(self.attack) + " HP>" + str(self.health))

#class monster 
class Monster:
    type = c.MONSTER      
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        #self.scream()
        
    def scream(self):
        print("WAAAAAA")  
    
    #will be fixed player and monster will inherit the same class    
    def show_stats(self):
        print("attack>" + str(self.attack) + " HP>" + str(self.health))

class Coms:
    def start_game(self):
        self.i_name = input("Zvol si své jméno: ")
        self.i_difficulty = input("Vyber obtížnost 1-5: ")
        
    def game_over(self):
        print("Dostali tě, zkus to znovu")
        
    def monster_dead(self, monster_name):
        print(monster_name + " byl poražen, pokračuješ dál")
        
def check_if_dead(character):
    notification = Coms()
    if character.health == 0:
        if character.type == c.MONSTER:
            notification.monster_dead(character.name)
        elif character.type == c.PLAYER:
            notification.game_over()
        else:
            print("Bad value")
        #print("game_over")
        return 1
    return 0



def encounter(monster, player, i = 0):

    #player atttacks a monster
    print(i)
    
    monster.health = monster.health - player.attack
    player.health = player.health - monster.attack
    i += 1
    
    if not check_if_dead(monster):
        print("monster live")
        if not check_if_dead(player):
            print("player live")
            encounter(monster, player)
    
    
    
    
    

chat = Coms()
chat.start_game()
player1 = Hero(chat.i_name, chat.i_difficulty)
monster1 = Monster("Vlk", 4, 5)
encounter(monster1, player1)




