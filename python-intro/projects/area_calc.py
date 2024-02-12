# comments are made with a hash

# standard input

# name = input('Tell me your name: ')
# age = input('... and your age: ')

# print('hello ' + name)
# print(name,'you are', age)


# Calc the area of a circle:
radius = input('Enter the radius of your circle (m)')
#area = 3.142 * radius**2 - this would throw error because radius is currently a string
area = 3.142 * int(radius)**2

print('The area of your circle is:', area)
