
def print_line_of_asterisks(num):
    # Prints a line of 'num' asterisks
    print(num * '* ')

def print_triangle_of_asterisks(num):
    # Prints a triangle of asterisks with a base of num
    for i in range(1, n+1):
        print_line_of_asterisks(i)


n = int(input("Give n: "))

print_triangle_of_asterisks(n)