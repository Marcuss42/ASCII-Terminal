from os import system
from time import sleep
from colorama import Fore, Style
from random import choice

COLORS = dir(Fore)[1:17]
COR_TELA = Fore.BLUE
DVD = 'DVD'
SIZE = len(DVD)

I, J = 11, 11
tela = [ [' ' * SIZE for j in range(J)] for i in range(I) ]

def main():
    vi, vj = 1, 2
    i, j = 1, 4

    while True:
        if i+vi >= I or i <= 0:
            vi = -vi
            cor_dvd = getattr(Fore,choice(COLORS))

        if j+vj >= J or j <= 0:
            vj = -vj
            cor_dvd = getattr(Fore,choice(COLORS))
            
        tela[i][j] = cor_dvd + DVD + COR_TELA
    
        print(COR_TELA + '█' * (2+J*SIZE))
        for linha in tela:
            print('█' + ''.join(linha) + '█')
        print('█' * (2+J*SIZE))
        
        tela[i][j] = ' ' * SIZE
        i += vi
        j += vj
        
        sleep(.5)
        system('cls || clear')

if __name__ == "__main__":
    system('cls || clear')
    try:
        main()
    except:
        print(Style.RESET_ALL)
    
