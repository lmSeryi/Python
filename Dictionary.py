dictionary = {}
dictionary['1st_element'] = 'Hola'
dictionary['2nd element'] = 'Adios'

print(dictionary['1st_element'])
print(dictionary['2nd element'])

grades = {}
grades['Geography'] = 9
grades['Data bases'] = 7
grades['Physics'] = 8
grades['POO'] = 9

for key in grades:
    print(key)

for value in grades.values():
    print(value)

for i in grades:
    print('Subject: {} : {}'.format(i, grades[i]))

total_ammount = 0

for grade in grades.values():
    total_ammount += grade

avg = total_ammount / len(grades.values())

print('The total ammount for your grades is: {}'.format(total_ammount))
print('Your average is: {}'.format(avg))
