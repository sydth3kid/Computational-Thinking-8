import turtle
t = turtle.Turtle()

# setup
t.speed(10)
turtle.Screen().bgcolor("light blue")


# stripes

# move to stripe 1
t.goto(-250, -100)
h = 100
f = 250
# stripe 1
t.color("white")
t.begin_fill()
t.forward(f)
t.left(90)
t.forward(h)
t.left(90)
t.forward(f)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()


# move to stripe 2
t.goto(-250, 0)

# stripe 2
t.color("red")
t.begin_fill()
t.forward(f)
t.left(90)
t.forward(h)
t.left(90)
t.forward(f)
t.left(90)
t.forward(h)
t.left(90)
t.end_fill()








turtle.exitonclick()
