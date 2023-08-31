myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
myTip = int(input("How much do you wanna tip? "))

tip = myTip * myBill / 100
answer = tip + myBill / numberOfPeople

print("You all owe", answer)