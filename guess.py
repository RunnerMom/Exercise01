# number guesser
# github question #1
import random

# greet player, get player name
name=raw_input("howdy! what is your name?")

# ask for guess
guess=0
# choose random number between 1 and 100

the_number=random.randint(1,100)
# while loop
tries=0
print the_number
while guess != the_number:
	guess=int(raw_input ("Your guess?"))
	tries +=1
	if guess < the_number:
		print "your guess is too low. Try higher."
	elif guess > the_number:
		print "your guess is too high. Try lower."
	else:
		print "Right on!! %s You found my number in %d guesses" % (name, tries)