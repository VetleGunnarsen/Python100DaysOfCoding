seconds_in_minute = 60
seconds_in_hour = 60 * seconds_in_minute
seconds_in_day = 24 * seconds_in_hour
seconds_in_year = 365.25 * seconds_in_day  # Account for leap years

while True:
    leapYear = input("Is it a leap year you are counting?")
    if leapYear == "yes" or leapYear == "Yes":
        print(seconds_in_year + seconds_in_day)
        break
    elif leapYear == "No" or leapYear == "no":
        print(seconds_in_year)
        break
    else:
        print("Try to answer again")
        continue
