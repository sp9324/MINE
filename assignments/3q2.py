day = int(input("Day-"))
month = int(input("Month-"))
year = int(input("Year-"))

if month == 2:
    if day == 28:
        print("next date is: 1/03/", year)
    else:
        print("next date is: ", day+1, "/02/", year)

elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    if day == 31 and month != 12:
        print("next date is: 1/", month+1, "/", year)
    elif day == 31 and month == 12:
        print("next date is: 1/01/", year+1)
    else:
        print("next date is: ", day+1, "/", month, "/", year)

elif month == 2 or month == 4 or month == 6 or month == 9 or month == 11:
    if day == 30:
        print("next date is: 1/", month+1, "/", year)
    else:
        print("next date is: ", day+1, "/", month, "/", year)
