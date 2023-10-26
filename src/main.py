import datetime

def is_leapyear(year):
    if (year < 0):
        year = datetime.datetime.now().year
        print("The year provided was below 0, it it now changed to the current year:",year)
    if (year % 4 == 0) and (year % 100 !=0) or (year % 400 == 0):
        return True
    if (year % 4 != 0) or (year % 100 == 0) and (year % 400 != 0):
        return False
    else:
        return False 

def main():
    first_try= is_leapyear(-1)
    print(first_try)

    first_try = is_leapyear(4000)
    print(first_try)

    first_try = is_leapyear(1800)
    print(first_try)
if __name__ == "__main__":
    main()


