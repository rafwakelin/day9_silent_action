from replit import clear
from art import logo

print(logo)
print("Welcome to th Silent Auction.\n")
	
apostas = {}
highest_bid = 0

while True:
	name = input("What's your name? ")
	bid = float(input("What is your bid? $"))
	next = input("Anyone else to bid? Yes or No? ").lower()
	
	apostas[name] = bid
	
	if next == 'no':
		break
	elif next == 'yes':
		next = True
		clear()
	else:
		print("Incorrect entry")
		break
clear()

for player in apostas:
	amount = apostas[player]
	if amount > highest_bid:
		highest_bid = amount
		winner = player
print (f" The winner of the auction is {winner} with a bid of ${highest_bid}. Congratulations!")