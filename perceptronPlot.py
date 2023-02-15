import tkinter
from math import e
import matplotlib.pyplot as plt
import numpy as np

puntitos =[]

#Interfaz
ventana = tkinter.Tk()
ventana.geometry("200x300")

etiqueta = tkinter.Label(ventana, text = "Elige tus pesos y bias\n")
etiqueta.pack()

#entradas
tkinter.Label(ventana, text="Peso 1.\n").pack()
peso1  =tkinter.Entry(ventana)
peso1.pack()

tkinter.Label(ventana, text="Peso 2\n").pack()
peso2  =tkinter.Entry(ventana)
peso2.pack()

tkinter.Label(ventana, text="Bias\n").pack()
bias  =tkinter.Entry(ventana)
bias.pack()

# Función de activación
def function_act(x, w, b):
    y = np.dot(x, w) + b
    if y >= 0:
        return 1
    else:
        return 0

def entrada_datos():
    pe1  = peso1.get()
    pe2  = peso2.get()
    b = bias.get()
    pes1 = float(pe1)
    pes2 = float(pe2)
    bia = float(b)
    
    weights = np.array([pes1, pes2])

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

def onclick(event):
    x, y = event.xdata, event.ydata
    puntitos.append([x, y])
    plt.scatter(x, y, color="black")
    plt.draw()

cid = fig.canvas.mpl_connect("button_press_event", onclick)

def draw_line(weights,bia):
    x = np.linspace(-10, 10, num=100)
    y = (-weights[0] * x - bia) / weights[1]
    plt.plot(x, y, "black")
    plt.show()
    draw_points(weights,bia)
    
def draw_points(weights,bia):
    for point in puntitos:
        x = np.array(point)
        y = function_act(x, weights, bia)
        color = "blue" if y >= 0.5 else "red"
        plt.scatter(point[0], point[1], color=color)

plt.show()

ventana.mainloop()
