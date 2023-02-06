import tkinter
import turtle
from math import e

W1 = 1
W2 = 1
B  = -1.5

ventana = tkinter.Tk()
ventana.geometry("500x500")

etiqueta = tkinter.Label(ventana, text = "Elige tus coordenadas")
etiqueta.pack()

coordenada1  =tkinter.Entry(ventana)
coordenada1.pack()

coordenada2  =tkinter.Entry(ventana)
coordenada2.pack()

def entrada_datos():
    co1  =coordenada1.get()
    co2  =coordenada2.get()
    cor1 = int(co1)
    cor2 = int(co2)
    draw_point(cor1,cor2)
    print(cor1,cor2)

def validar_color(x,y):

    result = (x*W1)+(y*W2)+B
    resultf = 1/(1+e**-result)
    print(resultf)

    if result >=0:
        return True
    elif result < 0:
        return False


entrada1  =tkinter.Button(ventana, text = "Poner", command = entrada_datos)
entrada1.pack()

entrada1  =tkinter.Button(ventana, text = "Calcular" command = draw_line)
entrada1.pack()

def draw_cartesian_plane():
    window = turtle.Screen()
    pen = turtle.Turtle()

    # Dibujar ejes X e Y
    pen.penup()
    pen.goto(-400, 0)
    pen.pendown()
    pen.goto(400, 0)
    pen.penup()
    pen.goto(0, 400)
    pen.pendown()
    pen.goto(0, -400)
    # Controlador de eventos de clic de ratón
    def on_click(x, y):
        pen.penup()
        pen.goto(x, y)
        pen.pendown()
        if validar_color(x,y):
            pen.dot(10, "blue")
        else:
            pen.dot(10, "red")
        print(x,y)
    window.onclick(on_click)


def draw_point(x1,y1):
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    if validar_color(x1,y1):
        pen.dot(10, "blue")
    else:
        pen.dot(10, "red")

def draw_line(x1,y1):
    window = turtle.Screen()
    pen = turtle.Turtle()
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()



draw_cartesian_plane()
ventana.mainloop()

