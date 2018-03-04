#The number guess game

import random

guessTaken=0
points=0
chance=0
totalpoints=0
guesses=10
i=0

print('.....................................................................APPROXIMATE TO THE BEST................................................................')
print('Hello!What is your name?')
name=input()
print('Hello, ' + name + ' Welcome to the game')
print('             RULES                 ')
print(' 1.You have to guess the number I choose\n 2.You will get 5 turns.\n 3.In each turn you will have 10 guesses.\n 3.If you guessed the number in first chance you earn 50 points,40 in 2nd guess,30 in 3rd ,20 in 4th,10 in 5th and 5 otherwise.\n 4.If you could not guess the number in 10 guesses you earn 0 points.\n 6.With each turn number of guesses decrease by 2\n 6.Total points will be given at last.') 
 
while chance<5:
	number=random.randint(1,50)
	
	print('       ***********************TURN NO.' + str(chance+1)+'*******************************')
	print('Well, '+ name +' I am thinking of numbers between 1 and 50')

	while guessTaken<guesses:
		print('Take a guess')
		guess=int(input())
		
	
		guessTaken=guessTaken+1
	
		if guess<=(number-10):
			print('Your guess is too low ')
	
		if guess<=(number-1)and guess>(number-10):
			print('Your guess is low ')
	
		if guess>=(number+10):
			print('Your guess is too high')
	
		if guess>=(number+1) and guess<(number+10):
			print('Your guess is high')
	
		if guess==number:
			break

	if guess==number:
		if guessTaken>5:
			print('Good job, '+ name + '! You guessed my number in ' + str(guessTaken) + ' guesses')
			points=points+5
			print('You earned  '+str(points) + ' points')
		if guessTaken==5:
			print('Good job, '+ name + '! You guessed my number in ' + str(guessTaken) + ' guesses')
			points=points+10
			print('You earned  '+str(points) + ' points')
			
		if guessTaken==4:
			print('Good job, '+ name + '! You guessed my number in ' + str(guessTaken) + ' guesses')
			points=points+20
			print('You earned '+str(points) + ' points')
			
		if guessTaken==3:
			print('Good job, '+ name + '! You guessed my number in ' + str(guessTaken) + ' guesses')
			points=points+30
			print('You earned '+str(points) + ' points')
			
		if guessTaken==2:
			print('Good job, '+ name + '! You guessed my number in ' + str(guessTaken) + ' guesses')
			points=points+40
			print('You earned '+str(points) + ' points')
			
		if guessTaken==1:
			print('Good job, '+ name + '! You guessed my number in ' + str(guessTaken) + ' guesses')
			points=points+50
			print('You earned '+str(points) + ' points')
				

	if guess!=number:
		print('Nope!, The number I was thinking of was, ' + str(number))
		print('You earn 0 points')
	chance=chance+1
	guessTaken=0
	totalpoints=points+totalpoints
	points=0
	guesses=guesses-2
	
	
print('****************************************************************RESULT****************************************************************')
if totalpoints>0:
	print('Congrats!!!You earned total '+ str(totalpoints) + ' points')
	print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$.....YOU WIN.....$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
if totalpoints==0:
	print('Sorry,You could not make any points.....\n Better Luck next time!!')
	print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^......YOU LOSE.....^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')