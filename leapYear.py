def is_leap(year):
    leap = False

    if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        print("is leap year")
        return True
    else:
        print("Is not leap year.")
        return False
    # Write your logic here

    return leap


year = int(input("input an year: "))

is_leap(year)