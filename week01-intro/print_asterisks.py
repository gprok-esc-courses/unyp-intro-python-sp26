# Ask user for a number (n) and print n asterisks

n = int(input("Give a number: ")) 

for i in range(0, n):
    print('*', end=' ')

print()

print(n * '* ')