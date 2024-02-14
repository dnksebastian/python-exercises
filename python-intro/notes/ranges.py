# for n in range(5):
#     print(n)

# for n in range(3, 10):
#     print(n)

# for n in range(0, 20, 4):
#     # this will go up to 20 (not including 20) in steps of 4
#     print(n)

burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']

# for n in range(len(burgers)):
#     print(n, burgers[n])

for n in range(len(burgers) - 1, -1, -1):
    # can also use range(-1, -1, -1) - both will start at the end and cycle through the list backwards
    print(n, burgers[n])