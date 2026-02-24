
file = open('data.csv')

lines = file.readlines() 

students = {} 

keys = lines[0].strip().split(',')
print(keys)

for line in lines[1:]:
    values = line.strip().split(',')
    student = {keys[0]: int(values[0]), keys[1]: values[1], keys[2]: float(values[2])}
    students[int(values[0])] = student

print(students)

