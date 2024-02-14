# FUNCTIONS

# def greet():
#     print('hello world')

# def greet(name, time):
#     print(f'Good {time} {name}, hope you are well')

# With default parameters:
# def greet(name = 'John', time = 'morning'):
#     print(f'Good {time} {name}, hope you are well')

# name = input('Enter your name: ')
# time = input('Enter the time of day: ')

# greet(name, time)

def area(radius):
    return 3.142 * radius * radius


def vol(area, length):
    print(area * length)

radius = int(input('Enter a radius: '))
length = int(input('Enter a length: '))

# area_calc = area(radius)
# vol(area_calc, length)

vol(area(radius), length)

