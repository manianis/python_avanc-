from turtle import Turtle, mainloop


# Déclaration d'une classe
class Rectangle:
    def __init__(self, x=0, y=0, width=480, height=320, fg="black", bg=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fg = fg
        self.bg = bg
    
    def dessiner(self):
        t.up()
        t.goto(self.x, self.y)
        t.down()
        t.color(self.fg, self.bg)
        t.begin_fill()
        for i in range(4):
            t.forward(self.width if i % 2 == 0 else self.height)
            t.right(90)
        t.end_fill()


t = Turtle()

# Instansiation
r1 = Rectangle(0, -50, 50, 50, bg='red')
r2 = Rectangle(0, 0, 50, 50, bg='green')
r3 = Rectangle(-50, 0, 50, 50, bg='blue')
r4 = Rectangle(-50, -50, 50, 50, bg='yellow')

r1.dessiner()
r2.dessiner()
r3.dessiner()
r4.dessiner()

mainloop()
