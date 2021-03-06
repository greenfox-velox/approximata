from tkinter import *
from math import *

canvas_width = 610
canvas_height = 610
python_green = "#476042"

master = Tk()

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

def create_hexa(xs, ys, size):
    s2 = sqrt(2)
    sizexplus = 1 / 2 * size
    sizeyplus = sqrt(3) / 2 * size
    points = [xs, ys, xs + size, ys, xs + size + sizexplus, ys + sizeyplus, xs + size, ys + 2 * sizeyplus, xs, ys + 2 * sizeyplus, xs - sizexplus, ys + sizeyplus]
    w.create_polygon(points, outline = python_green,
                fill = 'yellow', width = 2)

def create_fractalhexa(xs, ys, size):
    create_hexa(xs, ys, size)
    third = size / 3
    sizey2littleone = sqrt(3) / 3 * size
    if size < 10:
        pass
    else:
        create_fractalhexa(xs, ys, third)
        create_fractalhexa(xs + 2 * third, ys, third)
        create_fractalhexa(xs + 3 * third, ys + sizey2littleone, third)
        create_fractalhexa(xs - third, ys + sizey2littleone, third)
        create_fractalhexa(xs , ys + 2 * sizey2littleone, third)
        create_fractalhexa(xs + 2 * third, ys + 2 * sizey2littleone, third)

create_fractalhexa(155, 10, 300)

mainloop()
