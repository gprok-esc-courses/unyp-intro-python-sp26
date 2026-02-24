import csv 

file = open('data.csv')

reader = csv.DictReader(file)

students = {} 

for item in reader:
    item['id'] = int(item['id'])
    item['gpa'] = float(item['gpa'])
    students[item['id']] = item 

print(students)