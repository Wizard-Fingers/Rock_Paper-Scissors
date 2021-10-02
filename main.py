#v.1 Rock-Papper-Scissors project
print("Rock!")
print("Papper!")
print("Scissors!")

P1 = input("Player 1, Make a move: ").lower()
P2 = input("Player 2, Make a move: ").lower()

#tie
if P1 == P2:
  print("Its a tie!") 

#Game logic:

elif P1 == "rock" and P2 == "scissors":
  print("Player 1 wins!")
elif P1 == "scissors" and P2 == "rock":
  print("Player 2 wins!")

elif P1 == "scissors" and P2 == "papper":
  print("Player 1 wins!")
elif P1 == "papper" and P2 == "scissors":
  print("Player 2 wins!")

elif P1 == "papper" and P2 == "rock":
  print("Player 1 wins!")
elif P1 == "rock" and P2 == "papper":
  print("Player 2 wins!")

#in case of inpropper input

else:
  print("something went wrong...")