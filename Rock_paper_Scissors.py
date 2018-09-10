import sys
import getpass

print "Welcome to rock-paper-scissors! \n"

def playername():
	global player1
	global player2
	
	player1 = raw_input("Please enter Player name 1 :")
	player2 = raw_input("Please enter player name 2 :")
	
	menu()
	
def menu():
	choice = raw_input("\n What you want to do? \n" "1) Start a new Game \n" "2) Change Player name \n" "3) Quit the game \n" "Choose Option 1,2 or 3 \n")
	
	if choice == "1":
		newgame()
	elif choice == "2":
		playername()
	else:
		sys.exit("Invalid Input or option 3 chosen, quiting ...")
		
def newgame():
	print "Starting a new game of Rock Paper and Scissors"
	print  " Instructions : Use R(ock) or S(cissors) or P(aper) as Input"
	allowed = ["r","s","p"]
	
	while True :
		play1choice = getpass.getpass(prompt = "Player 1 :",stream=None)
		if play1choice not in allowed :
			print "Invalid choice Enter again:"
			continue 
		play2choice = getpass.getpass(prompt = "Player 2 :",stream=None)
		if play2choice not in allowed :
			print "Invalid choice Enter again:"
			continue 
		
		else:
			if play1choice == play2choice :
				print "\n It is a draw !"
				menu()
			
			elif play1choice == "r" and play2choice == "s" :
				print "\n %s won the game !" %player1
				
			elif play1choice == "p" and play2choice == "r" :
				print "\n %s won the game !" %player1	
				
			elif play1choice == "s" and play2choice == "p" :
				print "\n %s won the game !" %player1	
			
			else :
				print "\n %s won the game !" %player2
				
			menu()
playername()			