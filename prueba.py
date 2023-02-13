import matplotlib.pyplot as plt
import numpy as np

# Inicializar pesos y bias
weights = np.array([1, 1])
bias = -10

# Función de activación
def activation_function(x, w, b):
    y = np.dot(x, w) + b
    if y >= 0:
        return 1
    else:
        return 0

# Crear plano cartesiano
fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_title("Plano Cartesiano")

# Función que se ejecuta al hacer clic en el plano cartesiano
def onclick(event):
    x, y = event.xdata, event.ydata
    print("Coordenadas: ({:.2f}, {:.2f})".format(x, y))
    x = np.array([x, y])
    y = activation_function(x, weights, bias)
    color = "red" if y == 1 else "blue"
    plt.scatter(x[0], x[1], color=color)
    plt.draw()

# Conectar la función onclick con el evento button_press_event
cid = fig.canvas.mpl_connect("button_press_event", onclick)

# Dibujar la linea que divide los puntos
x = np.linspace(-10, 10, num=100)
y = (-weights[0] * x - bias) / weights[1]
plt.plot(x, y, "black")

# Mostrar el plano cartesiano
plt.show()
