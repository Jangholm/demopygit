from Enemy import Witch, Zombie, Dragon, Spider
from Player import Player
import random

class Fight:

    def create_enemies(self,):
        enemies_list = []
        witch = Witch()
        zombie = Zombie()
        dragon = Dragon()
        spider = Spider()
        enemies_list.append(witch)
        enemies_list.append(zombie)
        enemies_list.append(dragon)
        enemies_list.append(spider)
        enemy = random.choice(enemies_list)
        return enemy

    def action_player(self, enemy, player):
        print(f"{enemy}\nYour health: {player.health}")
        answer = input("A: Attack   L: Leave: ")
        if answer == "a":
            enemy.health -= player.attack
            return True
        elif answer == "l":
            return False


    def action_enemy(self, enemy, player):
        player.health -= enemy.attack

    def check_for_win(self, enemy):
        if enemy.health <= 0:
            print(f"\nYou defeated the {enemy.type}\n")
            return True
        else:
            return False

    def check_for_loss(self, player):
        if player.health <= 0:
            print("GAME OVER!!")
            return True
        else:
            return False



