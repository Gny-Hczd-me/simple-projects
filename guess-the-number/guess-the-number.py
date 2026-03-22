import random
choice=str(input("This is a game. First, you must choose an interval. Then, you will try to guess the number I have chosen.If you want to play enter \"yes\":\n"))
if choice=="yes" or choice=="Yes":
	print("Write interval:")
	first=int(input())
	last=int(input())
	numofattemps=int(input("write number of attemps:"))
	print(f"You have {numofattemps} attemps")
	numis=random.randint(first,last)
	while numofattemps>0:
		numofattemps-=1
		n=int(input("guess:"))
		if n==numis:
			print("congrats")
			break
		else:
			print("try again")
			print(f"You have {numofattemps} attempts.")