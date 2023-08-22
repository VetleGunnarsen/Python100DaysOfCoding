print("Are you a real star wars fan?")
print("-----------------------------")
print()

grandMaster = input("Who is the grand master of the jedi")
if grandMaster == "yoda":
  print("Nice, that one is easy")
  mother = input("Who gave birth to leia and luke?")
  if mother == "padme":
    print("Nice, last question")
    revan = input("What is the name of Darth Malecs master?")
    if revan == "darth revan":
      print("Congratz you are a real starwars fan!")
    else:
       print("Shame on you! You are no fan!")
  else:
    print("Shame on you! You are no fan!")
else:
  print("Shame on you! You are no fan!")