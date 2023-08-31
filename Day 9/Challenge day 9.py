#Challenge day 9. Make a program that decide what generation the user is.
while True:
    yearBorn = int(input("What year were you born in? "))
    if yearBorn >= 1925 and yearBorn <= 1946:
        print("Ah, a Traditionalist")
        break
    if yearBorn >= 1947 and yearBorn <= 1964:
        print("Ah, a Baby Boomer")
        break
    if yearBorn >= 1965 and yearBorn <= 1981:
        print("Ah, a Gen X")
        break
    if yearBorn >= 1982 and yearBorn <= 1997:
        print("Ah, a Millenial")
        break
    if yearBorn >= 1998 and yearBorn <= 2015:
        print("Ah, a Gen Z")
        break
    else:
        print("There is no name for this generation, try again")
        continue
