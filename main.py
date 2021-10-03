from random import randint
player = 0
computer = 0

while player < 2 and computer <2:
#v.4 Rock-Papper-Scissors project
  print(f"Your Score: {player}")
  print(f"Computer Score: {computer}")
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
      player += 1
    elif P2 == "paper":
      print("Computer wins")
      computer += 1
#paper
  elif P1 == "paper":
    if P2 == "rock":
      print("You win")
      player += 1
    elif P2 == "scissors":   
        print("Computer wins")
        computer += 1
#scissors
  elif P1 == "scissors":
    if P2 == "paper":
      print("You win")
      player += 1
    elif P2 == "rock":
      print("Computer wins")
      computer += 1
#in case of inpropper input
  else:
    print("something went wrong...")

if player > computer:
  print("Congrats, you win!")
else:
  print("O no you lost")

final_score = print(f"Your Score: {player} Computer Score: {computer}")