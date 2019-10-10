import random #this is a module in which the randint function is defined
print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("It's Player 1 Turn: " )

rand_num = random.randint(0,2)  #assigning the value to rand_num
#randint is a function which takes input as randint(start, end) so that it takes a random value between them

if rand_num == 0:
	Computer = "rock"
elif rand_num == 1:
	Computer = "paper"
else:                    #if not rock or paper it is only scissors
	Computer = "scissors"

print(f"Computer plays {Computer}")

if player1 == Computer:    #here in this if both of them give any wrong input then only else will be executed
	print("It's a tie")   # otherwise if only one player give wrong input nothing will be executed
elif player1 == "rock":
    if Computer == "scissors":
    	print("Player 1 wins")
    elif Computer == "paper":
    	print("Computer wins")
elif player1 == "paper":
    if Computer == "rock":
    	print("Computer wins")
    elif Computer == "scissors":
    	print("Computer wins")
elif player1 == "scissors":
	if Computer == "rock":
		print("Computer wins")
	elif Computer == "paper":
		print("Player 1 wins")
else:
	print("Something went wrong")

 
