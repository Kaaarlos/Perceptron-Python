import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

root = tk.Tk()
root.title("Perceptrón")

fig, ax = plt.subplots()
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)
ax.set_title("Plano Cartesiano")

points = []

def onclick(event):
    x, y = event.xdata, event.ydata
    points.append((x, y))
    plt.scatter(x, y, color="black")
    plt.draw()

def calculate_line(weight1, weight2, bias):
    x = [-10, 10]
    y = [-(weight1 * x[0] + bias) / weight2, -(weight1 * x[1] + bias) / weight2]
    return x, y

def classify_points(weight1, weight2, bias):
    for x, y in points:
        classification = weight1 * x + weight2 * y + bias
        if classification > 0:
            plt.scatter(x, y, color="blue")
        else:
            plt.scatter(x, y, color="red")
    plt.draw()

cid = fig.canvas.mpl_connect("button_press_event", onclick)

frame = tk.Frame(root)
frame.pack()

weight1_entry = tk.Entry(frame)
weight1_entry.pack(side="left")

weight2_entry = tk.Entry(frame)
weight2_entry.pack(side="left")

bias_entry = tk.Entry(frame)
bias_entry.pack(side="left")

def submit():
    weight1 = float(weight1_entry.get())
    weight2 = float(weight2_entry.get())
    bias = float(bias_entry.get())
    x, y = calculate_line(weight1, weight2, bias)
    plt.plot(x, y)
    classify_points(weight1, weight2, bias)

submit_button = tk.Button(frame, text="Submit", command=submit)
submit_button.pack(side="left")

canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_
