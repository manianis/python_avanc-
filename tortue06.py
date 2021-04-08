from turtle import Turtle, mainloop


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


class RoundedRectangle(Rectangle):
    def __init__(self,
                 x=0, y=0,
                 width=480, height=320,
                 fg="black", bg="",
                 radius=15):
        Rectangle.__init__(self, x, y, width, height, fg, bg)
        self.radius = radius

    def dessiner(self):
        t.up()
        t.goto(self.x + self.radius, self.y)
        t.down()
        t.color(self.fg, self.bg)
        t.begin_fill()
        w = self.width - self.radius
        h = self.height - self.radius
        for i in range(4):
            t.forward(w if i % 2 == 0 else h)
            t.circle(self.radius, 90)
        t.end_fill()


t = Turtle()

r1 = RoundedRectangle(0, -50, 50, 50, bg='red')
r1.dessiner()

mainloop()
