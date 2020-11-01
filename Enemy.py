class Enemy:
    def __init__(self, type, health, attack):
        self.type = type
        self.health = health
        self.attack = attack


class Witch(Enemy):
    def __init__(self,):
        super().__init__("Witch", 10, 6)

    def __str__(self):
        return f"\n___WITCH___\nHealth: {self.health}\n"

    def print_witch(self):
        print("||  ||\n\\()//\n //(__)\\\n||    ||")


class Dragon(Enemy):
    def __init__(self):
        super().__init__("Dragon", 10, 3)

    def __str__(self):
        return f"\n___Dragon___\nHealth: {self.health}\n"


class Zombie(Enemy):
    def __init__(self):
        super().__init__("Zombie", 6, 2)

    def __str__(self):
        return f"\n___ZOMBIE___\nHealth: {self.health}\n"


class Spider(Enemy):
    def __init__(self):
        super().__init__("Spider", 5, 1)

    def __str__(self):
        return f"\n___SPIDER___\nHealth: {self.health}\n"

