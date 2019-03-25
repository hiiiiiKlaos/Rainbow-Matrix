from colorama import init, Fore
from random import randint

init(autoreset=True)

value = input("How much random numbers would you like to generate? ")

for i in range(int(value)):
    randomColor = randint(1, 7)
    if randomColor == 1:
        print(Fore.RED + str(randint(0, 1)), end=" ")
    elif randomColor == 2:
        print(Fore.LIGHTRED_EX + str(randint(0, 1)), end=" ")
    elif randomColor == 3:
        print(Fore.YELLOW + str(randint(0, 1)), end=" ")
    elif randomColor == 4:
        print(Fore.GREEN + str(randint(0, 1)), end=" ")
    elif randomColor == 5:
        print(Fore.CYAN + str(randint(0, 1)), end=" ")
    elif randomColor == 6:
        print(Fore.MAGENTA + str(randint(0, 1)), end=" ")
    elif randomColor == 7:
        print(Fore.BLUE + str(randint(0, 1)), end=" ")

input()
