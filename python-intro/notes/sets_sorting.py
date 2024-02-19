# nums = [1, 4, 2, 7, 3, 8, 3, 4, 8, 1]

# print(sorted(nums))

# names = ['john', 'ryu', 'abe', 'Apple', 'ryan', 'john']

# print(sorted(names))


# sets:
# removes duplicates, doesnt preserve order

# print(set(nums))
# print(set(names))

# ninjas = {'ryu': 'black', 'yoshi': 'red', 'crystal': 'black'}
# ninjas.values()
# set(ninjas.values())

#####################################################

# def ninja_intro(dictionary):
#     for key, val in dictionary.items():
#         print(f'I am {key} and I am a {val} belt')

def belt_count(dictionary):
    belts = list(dictionary.values())

    for belt in set(belts): #this changes the list into set which removes duplicates
        num = belts.count(belt)
        print(f'There are {num} {belt} belts')

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

# ninja_intro(ninja_belts)

belt_count(ninja_belts)

