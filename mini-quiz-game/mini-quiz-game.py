from colorama import Fore, Style, init
init(autoreset=True)
questions={"What comes once in a minute, twice in a moment, but never in a thousand years?":"m","I am always in front of you, but can’t be seen. What am I?":"future","What goes up but never comes down?":"age","I fly without wings, i cry without eyes. Wherever i go, darkness flies. What am i?":"cloud","I have no life, but i can die. What am i?":"battery","What has words but never speaks?":"book","What can go through glass without breaking it?":"light","What comes down but never goes up?":"rain","What is belongs to you but is used more by others?":"name","What has cities, but no houses; rivers, but no water; and forests, but no trees?":"map"}
print(f'Welcome. There are {len(questions)} questions. If you answer at least 8 questions correctly, you will Win. Let\'s go. Good Luck \U0001F607 \n')
correct=0
length=len(questions)
num=0
while num<length:
	print('\n',list(questions.keys())[num])
	answer=input("-")
	if answer.lower()==list(questions.values())[num]:
		correct+=1
		print(Fore.GREEN+Style.DIM+"True \u2705")
	elif answer=="":
		print(" \u26A0 Please do not leave the answer blank. Enter something!")
		continue
	else:
		print(Fore.RED+Style.DIM+f"Wrong \u274c",f'True answer is {list(questions.values())[num]}')
	num+=1
print("\n")
print(f"Score is {correct}/{len(questions)}\n")
if correct==10:
	print("YOU ARE AMAZING \U0001F929 ")
elif correct>=8:
	print("\nCongrats. You Win \U0001F44F")
else:
	print("\nYou lost. Try again")
