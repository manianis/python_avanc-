from turtle import Turtle, mainloop, mode
import math


class Forme:
    def __init__(self, x=0, y=0, width=480, height=320, fg="black", bg=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.fg = fg
        self.bg = bg

    def dessiner(self):
        pass

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def translater(self, tx, ty):
        self.x += tx
        self.y += ty

    def reduire(self, cx, cy=None):
        if cy is None:
            cy = cx
        self.width *= cx
        self.height *= cy

    def __str__(self):
        return (self.__class__.__name__ + f"(x: {self.x}, y: {self.y}, "
                f"width: {self.width}, height: {self.height})")


class Rectangle(Forme):
    def __init__(self, x=0, y=0, width=480, height=320, fg="black", bg=""):
        Forme.__init__(self, x, y, width, height, fg, bg)

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
        w = self.width - 2 * self.radius
        h = self.height - 2 * self.radius
        for i in range(4):
            t.forward(w if i % 2 == 0 else h)
            t.circle(-self.radius, 90)
        t.end_fill()


class Ellipse(Forme):
    def __init__(self, x=0, y=0, width=480, height=320, fg="black", bg=""):
        Forme.__init__(self, x, y, width, height, fg, bg)

    def dessiner(self):
        t.up()
        t.color(self.fg, self.bg)
        t.begin_fill()
        r1 = self.width / 2
        r2 = self.height / 2
        xc, yc = self.x + r1, self.y - r2
        nticks = max(math.ceil(math.pi * max(r1, r2) / 15) // 2 * 2, 8)
        for i in range(2 * nticks + 1):
            x = xc + r1 * math.cos(i / nticks * math.pi)
            y = yc + r2 * math.sin(i / nticks * math.pi)
            t.goto(x, y)
            if i == 0:
                t.down()
        t.end_fill()


class FormeComposee(Forme):
    def __init__(self):
        Forme.__init__(self, 0, 0, 0, 0, "", "")
        self.formes = []

    def ajouter_forme(self, forme):
        if len(self.formes) == 0:
            self.x = forme.x
            self.y = forme.y
            self.width = forme.width
            self.height = forme.height
        else:
            fr, fb = forme.x + forme.width, forme.y + forme.height
            sr, sb = self.x + self.width, self.y + self.height
            self.x = forme.x if forme.x < self.x else self.x
            self.y = forme.y if forme.y < self.y else self.y
            self.width = max(fr, sr) - self.x
            self.height = max(fb, sb) - self.y

        self.formes.append(forme)

    def dessiner(self):
        for forme in self.formes:
            forme.dessiner()

    def translater(self, tx, ty):
        super().translater(tx, ty)
        for forme in self.formes:
            forme.translater(tx, ty)

    def set_position(self, x, y):
        ix, iy = self.x, self.y
        super().set_position(x, y)
        for forme in self.formes:
            forme.translater(x - ix, y - iy)

    def reduire(self, cx, cy=None):
        if cy is None:
            cy = cx
        ix, iy = self.x, self.y
        iw, ih = self.width, self.height
        super().reduire(cx, cy)
        for forme in self.formes:
            forme.set_position(ix + (forme.x - ix) * cx,
                               iy + (forme.y - iy) * cy)
            forme.reduire(cx, cy)


t = Turtle()

t.hideturtle()
t.speed(-1)

fc = FormeComposee()
fc.ajouter_forme(Ellipse(40, 40, 40, 40, bg='black'))
fc.ajouter_forme(Ellipse(120, 40, 40, 40, bg='black'))
fc.ajouter_forme(RoundedRectangle(0, 80, 200, 40, bg='orange', radius=5))
fc.ajouter_forme(Rectangle(40, 120, 120, 40, bg="lightblue"))
fc.ajouter_forme(Rectangle(-5, 65, 5, 10, bg="red"))
fc.dessiner()
print(fc)

fc.translater(-225, 0)
fc.dessiner()
print(fc)

fc.translater(0, -100)
fc.reduire(0.5)
fc.dessiner()
print(fc)

fc.translater(120, 0)
fc.dessiner()
print(fc)

fc.translater(120, 0)
fc.dessiner()
print(fc)

fc.translater(120, 0)
fc.dessiner()
print(fc)

fc.set_position(-230, 150)
fc.reduire(1.25)
fc.dessiner()
print(fc)

fc.set_position(-90, 150)
fc.dessiner()
print(fc)

mainloop()
