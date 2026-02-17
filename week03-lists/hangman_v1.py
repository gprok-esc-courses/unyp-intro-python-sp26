import random

words = ['inheritance', 'polymorphism', 'encapsulation',
         'composition', 'strategy', 'facade']

idx = random.randint(0, len(words)-1)
secret = words[idx]
print(secret)

print(secret[0], end='')
print('-' * (len(secret) - 2), end='')
print(secret[-1])