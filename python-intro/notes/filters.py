grades = ['A', 'B', 'F', 'C', 'F', 'A']

# filter(testing_function, data)

def remove_fails(grade):
    return grade != 'F'


# filter method:
print(list(filter(remove_fails, grades))) #typecasting into list


# for loop method:
filtered_grades = []

for grade in grades:
    if grade != 'F':
        filtered_grades.append(grade)

print(filtered_grades)

#comprehension method:
print([ grade for grade in grades if grade != 'F' ])