from turtle import Turtle, mainloop


def draw_rect(x, y, width, height):
    """Dessiner un rectangle

    Args:
        x (int): abcisse du coin supèrieur gauche
        y (int): ordonnée du coin supèrieur gauche
        width (int): Longueur en pixels
        height (int): Largeur en pixels
    """
    t.up()
    t.goto(x, y)
    t.down()
    for i in range(4):
        t.forward(width if i % 2 == 0 else height)
        t.right(90)


# PP
t = Turtle()

draw_rect(20, 20, 200, 100)

mainloop()
