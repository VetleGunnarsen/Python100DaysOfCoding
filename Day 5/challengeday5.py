varRunning = 0
hSolo = "Hello mr Han Solo"
oWan = "Hello there"
lOrgana = ""

print("Lets play the -What character from star wars are you- game")
print()
while varRunning == 0:
    swCharater1 = input("Are you humble?")
    if swCharater1 == "no":
        print("Haha! I guesst it!")
        print(hSolo)
        break
    else:
        print("Then u are not mr solo")

    swChartacter2 = input("Are you a jedi? ")
    if swChartacter2 == "yes":
        print("Haha! I know who you are")
        print(oWan)
        break
    else:
        print("Darn!")
