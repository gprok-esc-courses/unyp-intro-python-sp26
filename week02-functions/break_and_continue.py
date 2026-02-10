
# break - stops the loop
while True:
    print('Processing data ...')
    answer = input("Continue yes/no? ")
    if answer == "no":
        break


# continue - skips remaining code and goes to the next loop iteration
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)
    print("Odd number")