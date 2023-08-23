# Code below define a range
lower_bound = 1
divider_bound = 5
upper_bound = 10

print("This script will give you a ")
name = input("What is ur name? ")

if name == "vetle" or name == "Vetle":
  print("Hello Vetle!")
  feeling = input("How do you feel today on a scale from 1-10? ")
  number = int(feeling)
  if lower_bound <= number <= divider_bound:
    print("Hey", name + ",", """ just wanted to remind you that your smile has the power to light up even the cloudiest of days.""")
  elif divider_bound < number <= upper_bound:
    print("Well, aren't you a prime example of how evolution can occasionally take a coffee break?")
  elif number < lower_bound or number > upper_bound :
    print("I said between 1 and 10... are you stupid")
  elif not number.isdigit():
    print("A number please!")