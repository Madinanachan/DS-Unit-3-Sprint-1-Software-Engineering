"""
Class to represent Product
"""
import random


class Product:
    def __init__(self, name):
        self.name = name
        self.price = 10
        self.weight = 20
        self.flammability = .5
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        ratio = (self.price)/(self.weight)
        print(ratio)
        if ratio < .5:
            print('Not so stealable...')
        elif (ratio < 1) | (ratio >= .5):
            print('Kinda stealable.')
        else:
            print('Very stealable')
    
    def explode(self):
        explosion = (self.flammability)*(self.weight)
        if explosion < 10:
            print('...fizzle.')
        elif (explosion >= 10) & (explosion < 50):
            print('...boom!')
        else: 
            print('..BABOOM!!')

class BoxingGlove (Product): 
    def __init__(self, name = 'Boxing Glove'):
        super().__init__(name)
        self.weight = 10

    def explode(self):
        print('...its a glove.')

    def punch(self):
        if self.weight < 5:
            print('That tickles.')
        elif (self.weight >= 5) & (self.weight < 15):
            print('Stop hitting yourself')
        else:
            print('Ouch!')