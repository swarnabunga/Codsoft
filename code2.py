import random
print('Winning rules of the game ROCK PAPER SCISSORS are :\n'
	+ "Rock vs Paper -> Paper wins \n"
	+ "Rock vs Scissors -> Rock wins \n"
	+ "Paper vs Scissors -> Scissor wins \n")

while True:
	
	print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

	ch=int(input("Enter your choice :"))

	while ch > 3 or ch <1:
	    ch=int(input('Enter a valid choice please '))
		
	if ch == 1:
		ch_name= 'Rock'
	elif ch == 2:
		ch_name= 'Paper'
	else:
		ch_name= 'Scissors'
		
	print('User choice is \n',ch_name)
	print('Now its Computers Turn....')
	
	computer = random.randint(1,3)

	while computer == ch:
		computer = random.randint(1,3)
		
	if computer == 1:
		computer_name = 'rocK'
	elif computer == 2:
		computer_name = 'papeR'
	else:
		computer_name = 'scissoR'
	print("Computer choice is \n", computer_name)
	print(ch_name,'Vs',computer_name)

	if ch == computer:
		print('Its a Draw',end="")
		result="DRAW"

	if (ch==1 and computer==2):
		print('paper wins =>',end="")
		result='papeR'
	elif (ch==2 and computer==1):
		print('paper wins =>',end="")
		result='Paper'
		
	
	if (ch==1 and computer==3):
		print('Rock wins =>\n',end= "")
		result='Rock'
	elif (ch==3 and computer==1):
		print('Rock wins =>\n',end= "")
		result='rocK'
		
	if (ch==2 and computer==3):
		print('Scissors wins =>',end="")
		result='scissoR'
	elif (ch==3 and computer==2):
		print('Scissors wins =>',end="")
		result='Rock'

	if result == 'DRAW':
		print("<== Its a tie ==>")
	if result == ch_name:
		print("<== User wins ==>")
	else:
		print("<== Computer wins ==>")
	print("Do you want to play again? (Y/N)")

	ans = input().lower
	if ans =='n':
		break

print("thanks for playing")
