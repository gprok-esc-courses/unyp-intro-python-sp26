def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else: 
            return True 
    else: 
        return False

# Execute only if I eun this file.
# Do not execute if I import this file to another one
if __name__ == '__main__':
    year = int(input("Year to check: "))

    if is_leap_year(year):
        print("Leap Year")
    else: 
        print("Not a leap year")