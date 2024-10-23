import random

class Dice:
    def __init__(self, sides=3):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)


        #un simple dado con tres lados, me falta pensar que conviene que devuelva, por ahora devuelve el resultado.