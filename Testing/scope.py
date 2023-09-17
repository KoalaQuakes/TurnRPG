class Monster:
    def __init__(self,health,energy,mana,**kwargs):
        self.health = health
        self.energy = energy
        self.set_mana(mana)
        super().__init__(**kwargs)

    def udpate_energy(self,amount):
        self.energy += amount

    def set_mana(self,mana):
        new_mana = mana*2
        self.mana = new_mana

    def get_damage(self,amount):
        self.health -= amount

    def attack(self, amount):
        print(f'The Monster has attacked and dealt {amount} damage')
        self.energy -= 20

    def move(self,speed):
        print(f'The monster has moved with a speed of {speed} speed')


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

class Shark(Monster):
    def __init__(self, speed, health, energy, mana):
        super().__init__(health, energy, mana)
        #Monster.__init__(self, health, energy, mana)
        self.speed = speed

    def bite(self):
        print('the shark has bitten')

    def move(self):
        print('the shark has moved')
        print(f'the speed of the shark is {self.speed}')

shark = Shark(speed = 50, health = 90, energy = 75, mana = 45)
print(shark.mana, shark.bite())

class Scorpion(Monster):
    def __init__(self, poison, scorpion_health, scorpion_energy, scorpion_mana):
        super().__init__(scorpion_health, scorpion_energy, scorpion_mana)
        self.posion = poison

    def attack(self):
        print('The scorpion has attacked')
        print(f'it has dealt {self.posion} poison damage')

scorpion = Scorpion(poison = 50, scorpion_health = 20, scorpion_energy = 75, scorpion_mana = 50)
scorpion.attack()
scorpion.move(5)


class Fish:
    def __init__(self,speed,has_scales,**kwargs):
        self.speed = speed
        self.has_scales = has_scales
        super().__init__(**kwargs)

    def swim(self):
        print(f'the fish is swimming at a speed of {self.speed}')

# working with multiple inheritence
class Shark2(Monster, Fish):
    def __init__(self,bite_strength, health, energy, mana, speed, has_scales):
        self.bite_strength = bite_strength
        #print(Shark2.mro())
        super().__init__(health = health, energy = energy, mana = mana, speed = speed, has_scales = has_scales)

shark2 = Shark2(bite_strength = 50, health = 50, energy = 50, mana = 5, speed = 20, has_scales = False)
print(shark2.has_scales)