# ipsum_file = open('files/ipsum.txt')

##### using a loop:

# for line in ipsum_file:
#     print(line.rstrip())


##### using method readlines:
# ipsum_file.seek(0) #this goes back to the beginning of the opened file

# lines = ipsum_file.readlines()
# print(lines)


# ipsum_file.seek(50) #this will find 50th character in the file
# file_text = ipsum_file.read(100) #this will read 100 characters from the point set above

# print(file_text)

# ######closing files
# ipsum_file.close()



######### another method:

def sequence_filter(line):
    return '>' not in line

with open('files/dna_sequence.txt') as dna_file:
    lines = dna_file.readlines()
    print(list(filter(sequence_filter, lines)))

#carry on... no need to close the file