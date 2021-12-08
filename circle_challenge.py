import tkinter

def circle(page, radius, g, h, color="red"):
    page.create_oval(g + radius, h + radius, g - radius, h - radius, outline=color, width=2)


mainWindow = tkinter.Tk()


def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())


def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill="red")


mainWindow.title("Parabola")
mainWindow.geometry("640x480")
canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)
draw_axes(canvas)

circle(canvas, 100, 100, 100, "green2")
circle(canvas, 100, 100, -100)
mainWindow.mainloop()