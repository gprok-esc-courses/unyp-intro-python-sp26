import random 

secret = random.randint(1, 100)

print(secret)

# Keep number of guesses
counter = 0
user_guess = 0

while user_guess != secret:
    user_guess = int(input("Guess: "))
    counter = counter + 1
    if user_guess > secret:
        print('Go down')
    elif user_guess < secret:
        print('Go up')
    else:
        print(f'Found in {counter} guesses')
print('Bye!')
    