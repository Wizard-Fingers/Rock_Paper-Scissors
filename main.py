#v.2 Rock-Papper-Scissors project
print("Rock!")
print("Paper!")
print("Scissors!")
P1 = input("Player 1, Make a move: ").lower()
P2 = input("Player 2, Make a move: ").lower()
#Game logic:
#tie
if P1 == P2:
  print("Its a tie!") 
#rock
elif P1 == "rock":
  if P2 == "scissors":
    print("player1 wins")
  elif P2 == "paper":
    print("player2 wins")
#paper
elif P1 == "paper":
  if P2 == "rock":
    print("Player1 wins")
  elif P2 == "scissors":   
      print("Player2 wins")
#scissors
elif P1 == "scissors":
  if P2 == "paper":
    print("Player1 wins")
  elif P2 == "rock":
    print("Player2 wins")
#in case of inpropper input
else:
  print("something went wrong...")