# name = 'john'
# age = 20
# nums = [1,2,3,4]

# type(name)

# Class - a blueprint of how an object should look, not an object itself

from space.planet import Planet
from space.calc import planet_mass, planet_vol

naboo = Planet('Naboo', 300000, 8, 'Naboo System')

naboo_mass = planet_mass(naboo.gravity, naboo.radius)
naboo_vol = planet_vol(naboo.radius)

print(f'{naboo.name} has a mass of {naboo_mass} and a volume of {naboo_vol}')





# hoth = Planet('Hoth', 200000, 5.5, 'Hoth System')

# print(f'Name is: {hoth.name}')
# print(f'Radius is: {hoth.radius}')
# print(f'Gravity is: {hoth.gravity}')
# print(hoth.orbit())


# print(f'Name: {naboo.name}')
# print(f'Radius: {naboo.radius}')
# print(f'Gravity: {naboo.gravity}')
# print(naboo.orbit())

# print(Planet.shape)

# print(Planet.commons())

# print(Planet.spin()) #static method can me used on class itself
# print(Planet.spin('a very high speed')) #static method can me used on class itself
# print(naboo.spin('a very high speed')) #static method can me used on instances