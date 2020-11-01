class Player:
    def __init__(self, name=None, health=60, attack=3):
        self.name = name
        self.health = health
        self.attack = attack

    def create_player(self,):
        answer = input("Enter your name: ")
        print("")
        self.name = answer

