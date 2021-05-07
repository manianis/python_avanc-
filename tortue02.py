from turtle import Turtle, mainloop

# Dessiner un rectangle : 200 x 100
t = Turtle()
for i in range(4):
    t.forward(200 if i % 2 == 0 else 100)
    t.right(90)

mainloop()
