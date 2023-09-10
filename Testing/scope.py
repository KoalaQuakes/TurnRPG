class Monster:
    def __init__(self,health,energy,mana):
        self.health = health
        self.energy = energy
        self.set_mana(mana)

    def udpate_energy(self,amount):
        self.energy += amount

    def set_mana(self,mana):
        new_mana = mana*2
        self.mana = new_mana

    def get_damage(self,amount):
        self.health -= amount


monster = Monster(health = 100, energy = 50, mana = 50)

def update_health(amount):
    monster.health += amount

update_health(25)
monster.udpate_energy(13)
#monster.health += 20
print(monster.health, monster.energy, monster.mana)

class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster

    def attack(self):
        self.monster.get_damage(self.damage)

hero = Hero(damage = 15, monster = monster)
print(monster.health)

hero.attack()
print(monster.health)