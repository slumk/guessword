import process_module
import os
from colorama import Fore,Style

os.system('clear')

os.system("pyfiglet 'GuessWord'")
print("\n\t"+Fore.GREEN + 'Coded By @codedtrap')
print("\n\t"+Fore.GREEN + 'Instagram@Codedtrap')
print(Style.RESET_ALL)
rem_moves=10

while('_' in process_module.obf_word and rem_moves!=0):
    print("\n",*process_module.obf_word)
    print("\n","You Have",rem_moves,"Guesses Left")
    result=process_module.accept_move(input("\nEnter Your Guess:"))
    rem_moves-=1
    if result == 'notright':
        print("\nOh..You Missed..")
    elif result == 'exceed':
        print("\nYou Are Supposed To Enter A Character,Not A Word...")
        print("\nYou Missed A Move")
    elif result == "empty":
        print("\nYou Missed A Guess")
    elif result == "exnotright":
        print("You Tried The Same False Move...")
    else:
        print("\nYou Missed A Guess...")
    if process_module.tried_chars != []:
        print("You Have Tried [",*process_module.tried_chars,"]")


if '_' in process_module.obf_word and rem_moves==0:
    os.system('clear')
    print("\nGame Over,You Are Out Of Moves...")
    print("\nRestart Game Again..")
    os.system('exit')
else:
    os.system('clear')
    print("\nCONGRATS!!!You Won The Game...")
    print("\nIf You Liked This Game...Please Gimme A Star And Also Try To Give Feedbacks,That's How We All Improve")
    os.system('exit')
