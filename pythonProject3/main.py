from tkinter import *
import math

window = Tk()
window.title("Application")
window.geometry('500x500')

scale = Scale(window, orient = "horizontal", length = 100, width = 100, from_ = 0, to = 100, resolution = 1)
scale.pack()

c = Canvas(window, width=500, height=500, bg='white')
c.pack()

def on_click(event):
    x = event.x
    y = event.y
    r = scale.get()
    if y > 100:
        c.create_polygon(x-r*math.sqrt(2), y, x, y+r*math.sqrt(2), x+r*math.sqrt(2), y, x, y-r*math.sqrt(2), fill='green')
        c.create_oval(x - r, y - r, x + r, y + r, fill='red')

window.bind("<Button-1>", on_click)

window.mainloop()
