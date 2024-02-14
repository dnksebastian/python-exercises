# FOR LOOPS

# names = ['ryu', 'crystal', 'yoshi', 'ken']

# for name in names:
#     print(name)

# for name in names[1:3]:
#     print(name)

# for name in names:
#     if name == 'yoshi':
#         print(f'{name} - this is the selected name')
#     else:
#         print(name)

# for name in names:
#     if name == 'yoshi':
#         print(f'{name} - this is the selected name')
#         break # this escapes the loop
#     else:
#         print(name)


# WHILE LOOPS

age = 25
num = 0

while num < age:
    # this will repeat as long as the condition is true
    if num == 0:
        num += 1
        continue
    if num % 2 == 0:
        print(num)
    if  num > 10:
        break
    num +=1