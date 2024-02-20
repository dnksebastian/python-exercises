# name = 'john'
# age = 20
# nums = [1,2,3,4]

# type(name)

# Class - a blueprint of how an object should look, not an object itself

class Planet:
    
    def __init__(self):
        self.name = 'Hoth'
        self.radius = 200000
        self.gravity = 5.5
        self.system = 'Hoth System'

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

hoth = Planet()

print(f'Name is: {hoth.name}')
print(f'Radius is: {hoth.radius}')
print(f'Gravity is: {hoth.gravity}')
print(hoth.orbit())
