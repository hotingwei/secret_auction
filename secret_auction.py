from replit import clear
print("Welcome to secret auction room!")
secret_auction = {}
while True: 
	name = input("What is your name:\n")
	bid = str(input("How much do you want to bid:\n"))
	secret_auction[name] = bid
	new_bidder = input("Is there other bidders? Yes or No?").lower()
	if new_bidder == "no":
		break
	else:
		clear()


highest_bid = max(secret_auction[name])
winner = max(secret_auction)

print(f"The winner is {winner} with the highest bid {highest_bid}")
print(f"The participants are")
print(secret_auction)