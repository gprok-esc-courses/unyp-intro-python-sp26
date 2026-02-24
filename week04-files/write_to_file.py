
# file = open('courses.txt', 'w')
file = open('courses.txt', 'a')

while True:
    ans = input("Add course? y/n: ")
    if ans == 'n':
        break 
    course = input("Course title: ")
    file.write(f"{course}\n")

file.close()

