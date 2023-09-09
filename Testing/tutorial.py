class Monster:

    def __init__(self,health,energy):
        self.health = health
        self.energy = energy

    def __len__(self):
        return self.health

    def __abs__(self):
        return self.energy
    
    def __add__(self, other):
        self.health += other
        print(f'{self} has gained {other} health!')
        return self.health

    def __str__(self):
        return 'A monster'


    # Mehods
    def attack(self,amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= 20
        print(self.energy)

    def move(self,speed):
        print('The monster has moved')
        print(f'it has a speed of {speed}')

monster = Monster(health = 50, energy = 25)
monster.attack(40)
monster.move(15)

print(f"Monster has {monster.health} health")

print('The health of the monster is = ' + str(len(monster)))

monster + 55

print('The health of the monster is now = ' + str(monster.health))