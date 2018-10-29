#-*-coding: utf-8-*-
# Andres Zapata y Santiago Martinez, Octubre 2018

# Visualizacion de laberinto 4x4 a partir de
# una lista de literales. Cada literal representa una baldosa;
# el literal es positivo si hace parte de un camino solucion al laberinto.

# Formato de la entrada: - las letras proposionales seran: 1, ..., 16;
#                        - solo se aceptan literales (ej. 1, ~2, 3, ~4, etc.)
# Requiere tambien un numero natural, para servir de indice del laberinto resuelto,
# toda vez que puede solicitarse visualizar varios laberintos resueltos.

# Salida: archivo laberinto_%i.png, donde %i es un numero natural usado como indice

# Nota: Para ejecutar el programa use el siguiente comando:
#   python visualizacion.py [file.csv]
# donde file.csv contiene los literales solucion separados por comas
# y cada linea es una solucion diferente al mismo laberinto

def dibujar_tablero(f,m, n):
    # Visualiza laberinto dada una formula f
    # Input:
    #   - f, una lista de baldosas
    #   -m, una lista de muros
    #   - n, un numero de identificacion del archivo
    # Output:
    #   - archivo de imagen tablero_n.png

    # Inicializo el plano que contiene la figura
    fig, axes = plt.subplots()
    axes.get_xaxis().set_visible(False)
    axes.get_yaxis().set_visible(False)

    # Dibujo el laberinto
    step = 1./4
    tangulos = []
    inicio_fin = ['13','4']
    # Creo las baldosas del laberinto
    tangulos.append(patches.Rectangle(*[(0,0), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step, 0), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(2 * step, 0), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(3*step, 0), step, step],\
            facecolor='peachpuff'))
    tangulos.append(patches.Rectangle(*[(0, step), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step, step), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(2 * step, step), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(3*step, step), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(0,2*step), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(step, 2*step), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(2 * step, 2*step), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(3*step, 2 * step), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(0, 3*step), step, step],\
            facecolor='peachpuff'))
    tangulos.append(patches.Rectangle(*[(step, 3*step), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(2 * step, 3*step), step, step],\
            facecolor='cornsilk'))
    tangulos.append(patches.Rectangle(*[(3*step, 3 * step), step, step],\
            facecolor='cornsilk'))

    # Creo lineas que separan las baldosas
    for j in range(4):
        locacion = j * step
        # Crea linea horizontal
        tangulos.append(patches.Rectangle(*[(0, step + locacion), 1, 0.005],\
                facecolor='black'))
        # Crea linea vertical
        tangulos.append(patches.Rectangle(*[(step + locacion, 0), 0.005, 1],\
                facecolor='black'))
    # Agrego todos los elementos anteriores al plano
    for t in tangulos:
        axes.add_patch(t)

    # Modifico las baldosas que hacen parte del camino solucion
    letras_numeros = {'a':13,'b':14,'c':15,'d':16,'e':9,'f':10,'g':11,'h':12,'i':5,'j':6,'k':7,'l':8,'m':1,'n':2,'o':3,'p':4}
    for l in f:
        if '-' not in l and l not in inicio_fin:
            tangulos[letras_numeros[l]].set_facecolor("green")
    #Coloco los muros
    for l in f:
        if '-' in l and l[1] in m:
            tangulos[letras_numeros[l[1]] - 1 ].set_facecolor("black")
    # Genero el Output
    fig.savefig("laberinto_" + str(n) + ".png")

# Importando paquetes para dibujar
print "Importando paquetes..."
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
import csv
from sys import argv
print "Listo!"
