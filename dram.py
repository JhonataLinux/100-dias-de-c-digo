import tkinter as tk
root = tk.Tk()
root.title("Drawing Pad")
canvas = tk.Canvas(root, width=600, height=400, bg="white")

canvas.pack()

def draw(event):
    x, y = event.x, event.y
    r = 2  # raio do "pincel"
    canvas.create_oval(x - r, y - r, x + r, y + r, fill="black", outline="black")


canvas.bind("<B1-Motion>", draw)
root.mainloop()