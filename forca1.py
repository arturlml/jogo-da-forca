import sys 
import string 
import random 
def novo_jogo():
    print ('Bem-vindo ao Jogo da Forca')
    print ('Para iniciar um jogo, prima 1. Para sair, prima 0\n')
    escolha = int(raw_input('--> '))
    if not escolha:
        print ('\nAdeus!\n')
        sys.exit()
