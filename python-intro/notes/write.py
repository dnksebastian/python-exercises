with open('files/write.txt', 'w') as write_file: #second argument allows to write in the open file
    write_file.write('Hello there ninjas, python is awesome')
    write_file.write('\n I love it so much')

# some other code...

with open('files/write.txt', 'a') as write_file: # 'a' passed here ammends new instructions instead of overwriting them
    write_file.write('\n Should be in third line')


quotes = [
    '\nI can resist everything except temptation',
    '\nWe are all in the gutter, but some of us are looking at the stars',
    '\nAlways forgive your enemies - nothing annoys them so much'
]

with open('files/write.txt', 'a') as write_file:
    write_file.writelines(quotes)

