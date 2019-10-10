import random

random_number = random.randint(1,10)  #importing random module and generating random number b/n 1 t 10 and storing in variable


while True:
	user = input("Please enter a number between 1 and 10: ") #user input
	user = int(user)  #converting user input to integer value
	if user > random_number:
		print("Too High, Try again!")
	elif user < random_number:
		print("Too Low, Try again!")
	else:
		print("You have won!!!")
		user_info = input("Please confirm if you want to continue (y/n) ")  
		while user == random_number:
			if user_info != "y" and user_info != "n":
				user_info = input("Please confirm if you want to continue (y/n) ")
				continue
			elif user_info == "y": #if user want to play again we are generating the random number again
				random_number = random.randint(1,10)
				user = None #we are changing the value back to none
			else:
				print("Thanks for playing")
		break  #this break is to stop the parent while loop as the loop is defined for condition true

    



