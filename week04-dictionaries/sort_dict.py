
data = {3: 90, 5: 78, 1: 45, 8: 88, 4: 10}

for key in data:
    print(f"{key} = {data[key]}")

print(data.keys())
print(data.values())
print(data.items())

keys = list(data.keys())
print(keys)

sorted_keys = sorted(keys)
print(sorted_keys)

for key in sorted_keys:
    print(f"{key}: {data[key]}")