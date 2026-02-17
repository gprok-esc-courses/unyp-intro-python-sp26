
grades = [75, 98, 78, 82, 61, 77]

size = len(grades)
print(size)

print(grades[3])

# add an element at the end of the list
grades.append(67)
print(grades)

for i in range(0, len(grades)):
    print(grades[i])
print("==============")
for grade in grades:
    print(grade)
print("==============")

# Find grades less than 70
print("FAILED")
for grade in grades:
    if grade < 70:
        print(grade)

print(90 in grades)
print(82 in grades)

print(max(grades))
print(min(grades))

total = sum(grades)
size = len(grades)
print("Average:", total/size)
print(f"Average: {total/size}")