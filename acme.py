"""
Class to represent Product
"""
import random 

class Product:
    def __init__(self,name): 
        self.name=name
        self.price=10
        self.weight=20
        self.flammability=.5
        self.identifier=random.randint(1000000,9999999)
    
    def stealability(self):
        ratio=(self.price)/(self.weight)
        print(ratio)
        if ratio<.5: 
            print('Not so stealable...')
        elif (ratio<1) | (ratio>=.5): 
            print('Kinda stealable.')
        else: 
            print('Very stealable')
    
    def explode(self):
        explosion=(self.flammability)*(self.weight)
        if explosion<10:
            print('...fizzle.')
        elif (explosion>=10) & (explosion<50):
            print('...boom!')
        else: 
            print('..BABOOM!!')

class BoxingGlove (Product): 
    self.weight=10
    def __init__(self,name='Boxing Glove'):
        super().__init__(name)

    def explode(self):
        print('...its a glove.')

    def punch(self):
        if self.weight<5:
            print('That tickles.')
        elif (self.weight>=5) & (self.weight<15):
            print('Stop hitting yourself')
        else:
            print('Ouch!')
    
    """Change the default `weight` to 10 (but leave other defaults unchanged)
- Override the `explode` method to always return "...it's a glove."
- Add a `punch` method that returns "That tickles." if the weight is below 5,
  "Hey that hurt!" if the weight is greater or equal to 5 but less than 15, and
  "OUCH!" otherwise """