
data = [37, 3, 5, 18, 97, 23, 1, 6]

# data.sort()
# print(data)

# sorted_data = sorted(data)
# print(data)
# print(sorted_data)

# BUBBLE SORT 

stop = len(data) - 1
for i in range(len(data)-1):
    for j in range(stop):
        # print(j, end=' ')
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]
    # print()
    stop -= 1

print(data)