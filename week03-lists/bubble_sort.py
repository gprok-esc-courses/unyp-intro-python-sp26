
data = [73, 14, 33, 4, 21, 67, 45, 12, 27, 16, 3, 31]

size = len(data)
stop = size-1

for it in range(0, size-1):
    for pos in range(0, stop):
        if data[pos] > data[pos+1]:
            data[pos], data[pos+1] = data[pos+1], data[pos]
    stop -= 1

print(data)

