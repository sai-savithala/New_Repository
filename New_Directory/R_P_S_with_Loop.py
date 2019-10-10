#here we are looping the game as per the winning score that we want and whoever gets to winning score first will win
import random #this is a module in which the randint function is defined

player_win = 0  #declaring value as 0 as we need to count player win
computer_win = 0 #declaring value as 0 as we need to count computer win
winning_score = 3  #we can change the winning score value as we want
 
while player_win < winning_score and computer_win < winning_score:
	print("Rock...")
	print("Paper...")
	print("Scissors...")
	print(f"computer score:{computer_win} and player score:{player_win}") #to display the points

	player1 = input("It's Player 1 Turn: " ).lower()  #converts upper case to lower 
	if player1 == "quit" or player1 == "q":  #this is if the user want to quit the game
		break
	if player1 != "rock" and player1 != "scissors" and player1 != "paper": #if we donot give a valid input then the loop starts from the first as we gave continue
		print("Please enter a valid input")
		continue #this makes sure that if valid input is not given loop will start from first
	elif player1 == "rock" or player1 == "scissors" or player1 == "paper":
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
		    	player_win+=1 #we are incrementing the player win count by 1 here as player1 wins
		    elif Computer == "paper":
		    	print("Computer wins")
		    	computer_win+=1 #we are incrementing computer win by 1
		elif player1 == "paper":
		    if Computer == "rock":
		    	print("Player1 wins")
		    	player_win+=1 #we are incrementing player win by 1
		    elif Computer == "scissors":
		    	print("Computer wins")
		    	computer_win+=1 #we are incrementing computer win by 1
		elif player1 == "scissors":
			if Computer == "rock":
				print("Computer wins")
				computer_win+=1 #we are incrementing computer win by 1
			elif Computer == "paper":
				print("Player 1 wins")
				player_win+=1 #we are incrementing player win by 1
				
		else:
			print("Something went wrong")
	else:
		break
#after the player or the computer wins 2 times the loop stops and executes below code
if player_win > computer_win:
	print("Hurray!!! You won")
elif player_win < computer_win:
	print("Sorry you have lost :( Please try again")
else:
	print("Oops..It's a tie..")
    
    


 
