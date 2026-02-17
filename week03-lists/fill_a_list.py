import random

data = []
for i in range(10):
    data.append(0)

print(data)

# Try the pythonian way

data2 = [0] * 10
print(data2)

# Fill a list with random values
data = []
for i in range(10):
    data.append(random.randint(10, 99))
print(data)

data2 = [random.randint(10, 99) for i in range(10)]
print(data2)