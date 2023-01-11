from colorama import Fore
from time import sleep
from random import randint

colors = dir(Fore)[:17]
len_colors = len(colors)

try:
    while True:
        for color in colors:
            print(eval(f"Fore.{color}") + ' '*randint(1, 150) + "a")
            sleep(.03)
except (KeyboardInterrupt, AttributeError):
    print(Fore.RESET)
