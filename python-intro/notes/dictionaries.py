# ninja_belts = {"crystal": "red", "ryu": "black"}

# print(ninja_belts["crystal"])

# key in dict
# 'yoshi' in ninja_belts # is false

# ninja_belts.keys()
# list(ninja_belts.keys())

# ninja_belts.values()
# vals = list(ninja_belts.values())

# vals.count('black')
# vals.count('blue')

# ninja_belts['yoshi'] = 'red'

# person = dict(name = 'john', age = 27, height = '6ft')

#####################################################################
def ninja_intro(dictionary):
    for key, val in dictionary.items():
        print(f'I am {key} and I am a {val} belt')

ninja_belts = {}

while True:
    ninja_name = input('enter a ninja name: ')
    ninja_belt = input('enter a belt color: ')
    ninja_belts[ninja_name] = ninja_belt

    another = input('add another? (y/n) ')
    if another == 'y':
        continue
    else:
        break

ninja_intro(ninja_belts)