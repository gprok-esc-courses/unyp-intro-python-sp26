
try:
    file = open('some_file.txt')
except:
    print("File not found")
    ans = input("Create the file? y/n: ")
    if ans == 'n':
        exit(0)
    else: 
        file = open('some_file.txt', 'w')
        file.close()
        file = open('some_file.txt')

lines = file.readlines()

if len(lines) == 0:
    print("File is empty")
else:
    for line in lines:
        print(line)