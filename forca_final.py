import turtle

window = turtle.Screen()    
window.setup(width=1400,startx=None, starty=None)
window.bgcolor("magenta")
window.title("Forca")
desenho = turtle.Turtle()
def desenhar_tracos():
    desenho = turtle.Turtle()
    desenho.hideturtle()    
    desenho.penup()    
    desenho.setpos(-300,-90)       
    desenho.write(senha, move=False, align="left", font=("Times", 45, "normal"))
    
def contrucao_base():
    desenho = turtle.Turtle()
    desenho.speed(2)
    desenho.pensize(10)
    desenho.back(300)
    desenho.penup()    
    desenho.left(90)
    desenho.pendown()
    desenho.forward(300)
    desenho.penup()
    desenho.right(90)
    desenho.pendown()
    desenho.forward(120)
    desenho.penup()
    desenho.right(90)
    desenho.pendown()
    desenho.forward(110)

def construcao_cabeca():
   
        desenho = turtle.Turtle()          
        desenho.speed(5)
        desenho.pensize(10)
        desenho.penup()
        desenho.setpos(-180,180)
        desenho.left(180)
        desenho.pendown()
        desenho.circle(22)
        desenho.color("black")
        desenho.hideturtle()
def corpo():
        desenho = turtle.Turtle()          
        desenho.speed(5)
        desenho.pensize(5)
        desenho.penup()
        desenho.setpos(-180,40)
        desenho.left(90)
        desenho.pendown()
        desenho.forward(100)
        desenho.color("black")

def bracoum():
    desenho=turtle.Turtle()
    desenho.speed(5)
    desenho.pensize(5)
    desenho.penup()
    desenho.setpos(-180,120)
    desenho.pendown()
    desenho.right(135)
    desenho.forward(40)
    desenho.color("black")

def bracodois():
    desenho=turtle.Turtle()
    desenho.speed(5)
    desenho.pensize(5)
    desenho.penup()
    desenho.setpos(-180,120)
    desenho.pendown()
    desenho.right(400)
    desenho.forward(40)
    desenho.color("black")

def perna_um():
    desenho=turtle.Turtle()
    desenho.speed(5)
    desenho.pensize(5)
    desenho.penup()
    desenho.setpos(-180,40)
    desenho.pendown()
    desenho.right(400)
    desenho.forward(40)
    desenho.color("black")

def perna_dois():
    desenho=turtle.Turtle()
    desenho.speed(5)
    desenho.pensize(5)
    desenho.penup()
    desenho.setpos(-180,40)
    desenho.pendown()
    desenho.right(490)
    desenho.forward(40)
    desenho.color("black")

     


import random
arquivo = open('Pasta2.csv','r')
leitura=arquivo.read(1000)
lista = leitura.split(';')
palavra = random.choice(lista)

for x in range(100):
     print()
digitadas = []
acertos = []
erros = 0
while True:
    senha = ""    
    for letra in palavra:
        senha += letra if letra in acertos else "_ "
        desenhar_tracos()
        
    if senha == palavra:
        print('vc acertou')
        break
    chute= window.textinput('','Digite uma letra ')
    
    
    if chute == ('sair'):
        break
    if chute in digitadas:
        print('voce ja digitou essa letra')
        
        continue
    else:
        digitadas += chute
        
    if chute in palavra:
        acertos += chute
            
    else:
            erros += 1
            print("Você errou!")
            contrucao_base()
            
    if erros >= 1:
             construcao_cabeca()
     
             linha2 = ""
    if erros == 2:
            corpo()
    elif erros == 3:
            bracoum()
    elif erros >= 4:
            bracodois() 
    if erros == 5:
            perna_um()
    elif erros >= 6:
            perna_dois()
    if erros == 6:
        def perdeu():
            desenho = turtle.Turtle()
            desenho.hideturtle()    
            desenho.penup()    
            desenho.setpos(0,20)       
            desenho.write('perdeu', move=False, align="left", font=("Times", 50, "normal"))
        perdeu()    
        break
window.exitonclick()