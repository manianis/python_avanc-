from turtle import Turtle, mainloop


def draw_rect(x, y, width, height, fg="black", bg=""):
    """Dessiner un rectangle

    Args:
        x (int): abcisse du coin supèrieur gauche
        y (int): ordonnée du coin supèrieur gauche
        width (int): Longueur en pixels
        height (int): Largeur en pixels
        fg (str): couleur de tracé
        bg (str): couleur d'arrière plan
    """
    t.up()
    t.goto(x, y)
    t.down()
    t.color(fg, bg)
    t.begin_fill()
    for i in range(4):
        t.forward(width if i % 2 == 0 else height)
        t.right(90)
    t.end_fill()


# PP
t = Turtle()
t.speed(0)

draw_rect(-140, 110, 280, 280)

for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            draw_rect(i*30 - 120, j*30 - 120, 30, 30, "black", "black")
        else:
            draw_rect(i*30 - 120, j*30 - 120, 30, 30)

mainloop()
