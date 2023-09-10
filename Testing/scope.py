class Monster:
    def __init__(self,health,energy):
        self.health = health
        self.energy = energy

monster = Monster(health = 100, energy = 50)

def update_health(amount):
    monster.health += amount

update_health(25)

#monster.health += 20
print(monster.health)