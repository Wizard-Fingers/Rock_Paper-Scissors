from random import randint
#v.3 Rock-Papper-Scissors project
print("Rock!")
print("Paper!")
print("Scissors!")
P1 = input("Make a move: ").lower()
#Random selection based on import random
P2 = randint(0,2)
if P2 == 0:
  P2 = "rock"
elif P2 == 1:
  P2 = "paper"
else:  
  P2 = "scissors"
#Game logic:
#tie
if P1 == P2:
  print("Its a tie!") 
#rock
elif P1 == "rock":
  if P2 == "scissors":
    print("You win")
  elif P2 == "paper":
    print("Computer wins")
#paper
elif P1 == "paper":
  if P2 == "rock":
    print("You win")
  elif P2 == "scissors":   
      print("Computer wins")
#scissors
elif P1 == "scissors":
  if P2 == "paper":
    print("You win")
  elif P2 == "rock":
    print("Computer wins")
#in case of inpropper input
else:
  print("something went wrong...")