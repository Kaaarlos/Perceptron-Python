import tkinter
from math import e
import matplotlib.pyplot as plt
import numpy as np
import random
import time

puntitos =[]
uno_cero=[]

#Interfaz
ventana = tkinter.Tk()
ventana.geometry("200x300")

# Función de activación
def function_act(w,x,b):
    z = w * x
    if z.sum()  + b > 0:
        return 1
    else:
        return 0

def entrada_datos():

    weights = np.random.uniform(-1,1,size=2)
    bia = np.random.uniform(-1,1) 
    tasa_aprendizaje = 0.01
    epocas = 100

    for epoca in range(epocas):
        error_total = 0
        for i in range(len(puntitos)):
            prediccion=function_act(weights,puntitos[i],bia)
            error = uno_cero[i] - prediccion
            error_total += error**2
            weights[0] += tasa_aprendizaje * puntitos[i][0] * error
            weights[1] += tasa_aprendizaje * puntitos[i][1] * error
            
            bia += tasa_aprendizaje * error
        print(error_total,end=" ")
        draw_line(weights,bia)



entrada1  =tkinter.Button(ventana, text = "Calcular",command = entrada_datos)
entrada1.pack()

#Grafica
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_title("Plano Cartesiano")

#Linea horizontal
ax.axhline(y=0, color='black', lw=2)

#Linea vertical
ax.axvline(x=0, color='black', lw=2)

def draw_plane():
    plt.cla()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-10, 10)
    ax.set_title("Plano Cartesiano")
    #Linea horizontal
    ax.axhline(y=0, color='black', lw=2)

    #Linea vertical
    ax.axvline(x=0, color='black', lw=2)
    

def onclick(event):
    x, y = event.xdata, event.ydata
    puntitos.append([x, y])
    if event.button == 1:
        print("Se hizo clic izquierdo")
        uno_cero.append(1)
    elif event.button == 3:
        print("Se hizo clic derecho")
        uno_cero.append(0)
    print(puntitos)
    print(uno_cero)
    plt.scatter(x, y, color="black")
    plt.draw()

cid = fig.canvas.mpl_connect("button_press_event", onclick)

def draw_line(weights,bia):
    print(1)
    x = np.linspace(-10, 10, num=100)
    y = (-weights[0] * x - bia) / weights[1]
    draw_plane()
    plt.plot(x, y, "red")
    plt.show()
    draw_points(weights,bia)
    plt.draw()
    plt.pause(0.001) 
    
def draw_points(weights,bia):
    for point in puntitos:
        x = np.array(point)
        y = function_act(x, weights, bia)
        color = "blue" if y >= 0.5 else "red"
        plt.scatter(point[0], point[1], color=color)

plt.show()

ventana.mainloop()
