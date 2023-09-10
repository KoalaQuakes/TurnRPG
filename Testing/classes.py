class Monster:
    def __init__(self,func):
        self.func = func

class Attacks:
    def __init__(self) -> None:
        pass

    def bite(self):
        print('Bite has bitten')

    def strike(self):
        print('Stike has struck')

    def slash(self):
        print('Slash has slashed')

    def kick(self):
        print('Kick has kicked')

attacks = Attacks()
monster = Monster(attacks.bite())