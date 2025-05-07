from random import *

base = open("basededatos.txt", "r")
contenido = base.read()
frases = contenido.split("\n")
x = randint(0,len(frases)-1)
frase = frases[x]
visual = ""
listafrase = []
listavisual = []
vida = 3
letras = ""
otralistamas = frase.split()

for i in frase:
    if i == " ":
        x = " "
    else:
        x = "_"
        
    visual+=x    
    listavisual.append(x)
    listafrase.append(i)
    

while visual != frase and vida > 0:
    print(visual)
    letra = input("Escribe tu respuesta: ")

    if letra == frase:
        print("Ganastes!!", frase)
        break
    elif letra not in frase:
        print(f""""{letra}" No esta en la frase. vidas: {vida-1}""")
        vida-=1
        if vida == 0:
            print(f"""Perdistes, la frase era "{frase}".""")
    elif letra in letras:
        print(f"Ya usastes esa letra. vidas {vida-1}")
        vida-=1
        if vida == 0:
            print(f"""Perdistes, la frase era "{frase}".""")
    else:
        y=0
        visual=""
        for i in listafrase:
            if letra == i:
                listavisual[y] = i
            visual+=listavisual[y]
            y+=1
        letras+=letra
        
if visual == frase:
    print("Ganastes!!", frase)