from colorama import Fore
from random import choice, randrange
from string import ascii_letters as alfabeto
from time import sleep
from os import system
from keyboard import is_pressed

class Dvl:
    def __init__(self, I=10, J=7):
        self.I, self.J = I, J

        self.jogador = Jogador(5, f"{Fore.GREEN}0", (I-1, J//2))
        self.tela_fundo = " "
        self.mapa = [[self.tela_fundo for _ in range(J)] for _ in range(I)]

        self.VELOCIDADE_JOGADOR = 1
        self.FREQUENCIA_OBSTACULO = 3
        self.contador_obstaculo = 0

        self.score = 0

    def mostrar_mapa(self, tab=0):
        tab = tab * " "
        cor_margem=Fore.YELLOW

        for i in self.mapa:
            print(f"{cor_margem}{tab}|{f''.join(i)}", end=f"{cor_margem}|\n")
        print(f"""{Fore.LIGHTMAGENTA_EX}VIDA: {Fore.CYAN}{self.jogador.vida}
{Fore.LIGHTMAGENTA_EX}SCORE: {Fore.CYAN}{self.score}""")

    def mover_obstaculos(self):
        for i in range(self.I-1, 0, -1):
            aux = self.mapa[i]
            self.mapa[i] = self.mapa[i-1]
            self.mapa[i-1] = aux

    def gerar_obstaculo(self):
        obstaculo = randrange(0, self.J)
        self.mapa[0][obstaculo] = f"{Fore.RED}{choice(alfabeto)}"

    def update(self):
        system("cls")

    def mover_jogador(self, direcao):
        jg = self.jogador
        if direcao == 'd':
            jg.y += self.VELOCIDADE_JOGADOR
        elif direcao == 'a':
            jg.y -= self.VELOCIDADE_JOGADOR

        jg.y = max(0, min(jg.y, self.J-1))

    def verificar_teclas_pressionadas(self):
        if is_pressed('d'):
            self.mover_jogador('d')
        elif is_pressed('a'):
            self.mover_jogador('a')

    def verificar_colisao(self):
        return self.mapa[self.jogador.x-1][int(self.jogador.y)] != self.tela_fundo
    
    def verificar_morte(self):
        return self.jogador.vida == 0
            
    def main(self):
        jg = self.jogador

        while True:
            self.contador_obstaculo += 1
            self.score += 10
            if self.contador_obstaculo % self.FREQUENCIA_OBSTACULO == 0:
                self.gerar_obstaculo()

            self.mapa[jg.x][int(jg.y)] = f"{Fore.GREEN}{jg}"
           
            self.mostrar_mapa()

            self.verificar_teclas_pressionadas()

            if self.verificar_colisao():
                jg.vida -= 1

                if self.verificar_morte():
                    print(f"{Fore.RED}\nMORREU!{Fore.RESET}")
                    break
          
            self.mapa[jg.x] = [self.tela_fundo] * self.J

            self.mover_obstaculos()
            sleep(0.05)
            self.update()

class Jogador:
    def __init__(self, vida, c, pos):
        self.vida = vida
        self.c = c
        self.pos = pos
        self.x = pos[0]
        self.y = pos[1]

    def __str__(self):
        return self.c

if __name__ == "__main__":
    try:
        dlv = Dvl(14)
        dlv.main()
    except Exception as e:
        print(Fore.RESET, e)
