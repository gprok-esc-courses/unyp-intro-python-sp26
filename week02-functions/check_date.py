from leap_year import is_leap_year

def is_correct_date(day, month, year):
    # Check month between 1-12
    if month >= 1 and month <= 12:
        if month in (1, 3, 5, 7, 8, 10, 12):
            if day >= 1 and day <= 31:
                return True
            else:
                return False
        elif month in (4, 6, 9, 11):
            if day >= 1 and day <= 30:
                return True
            else:
                return False  
        else:  # February
            if is_leap_year(year):
                if day >= 1 and day <= 29:
                    return True
                else:
                    return False
            else:
                if day >= 1 and day <= 28:
                    return True
                else:
                    return False
    else:
        return False


if __name__ == '__main__':
    day = int(input("Day: ")) 
    month = int(input("Month: ")) 
    year = int(input("Year: "))

    if is_correct_date(day, month, year):
        print("Correct")
    else:
        print("Wrong")

